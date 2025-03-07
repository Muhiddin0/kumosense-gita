import click
import itertools
import sys
import time
import threading
from .git_helper import get_diff, commit_and_push_git, commit_git
from .commit import generate_commit_message


@click.group()
def cli():
    """Gita - AI yordamida avtomatik commit yozish CLI"""
    pass


def loading_animation(event):
    """Yuklanish animatsiyasini ko'rsatadi."""
    animation = itertools.cycle(
        ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])

    while not event.is_set():
        sys.stdout.write(f"\r🤖 AI model yuklanmoqda... {next(animation)} ")
        sys.stdout.flush()
        time.sleep(0.1)

    # Tozalash uchun bo'sh joy qo'shildi
    sys.stdout.write("\r✅ AI model yuklandi!          \n")
    sys.stdout.flush()


@click.command()
@click.option('--push', is_flag=True, help="Commitdan keyin avtomatik push qilish")
@click.option('--use-sticker', is_flag=True, help="Commit xabari oldiga emoji yoki sticker qo'shish")
def commit(push, use_sticker):
    """AI tomonidan avtomatik commit yozish"""

    diff = get_diff()

    if not diff.strip():
        print("❌ Hech qanday o'zgarish topilmadi. Commit kerak emas.")
        return

    # AI Model API chaqirishdan oldin animatsiya boshlash
    stop_event = threading.Event()
    loader_thread = threading.Thread(
        target=loading_animation, args=(stop_event,))
    loader_thread.start()

    # AI modeldan commit xabarini olish
    try:
        message = generate_commit_message(
            changes=diff, use_sticker=use_sticker)
    except ValueError as e:
        print(f"❌ {e}")
        return

    # Animatsiyani to'xtatish
    stop_event.set()
    loader_thread.join()

    if push:
        commit_and_push_git(message)
    else:
        commit_git(message)


cli.add_command(commit)

if __name__ == "__main__":
    cli()
