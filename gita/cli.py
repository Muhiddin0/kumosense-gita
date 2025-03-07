import click
import threading
import sys
import time
from .git_helper import get_diff, commit_and_push_git, commit_git
from .commit import generate_commit_message


def show_loading(stop_event):
    """Loading animatsiyasini konsolda ko‘rsatish"""
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write(
            f"\r⏳ AI commit xabarini generatsiya qilmoqda... {animation[idx % len(animation)]}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    # Ekranni tozalash
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


@click.group()
def cli():
    """Gita - AI yordamida avtomatik commit yozish CLI"""
    pass


@click.command()
@click.option('--push', is_flag=True, help="Commitdan keyin avtomatik push qilish")
@click.option('--use-sticker', is_flag=True, help="Commit xabari oldiga emoji yoki sticker qo'shish")
def commit(push, use_sticker):
    """AI tomonidan avtomatik commit yozish"""
    diff = get_diff()

    if not diff.strip():
        click.echo("❌ Hech qanday o'zgarish topilmadi. Commit kerak emas.")
        return

    # Thread uchun stop event
    stop_event = threading.Event()

    # Loading animatsiyasini alohida threadda ishga tushirish
    loading_thread = threading.Thread(
        target=show_loading, args=(stop_event,), daemon=True)
    loading_thread.start()

    # AI modeldan commit xabarini olish
    try:
        message = generate_commit_message(
            changes=diff, use_sticker=use_sticker)
    except ValueError as e:
        stop_event.set()
        loading_thread.join()
        click.echo(f"❌ AI commit yaratishda xatolik: {e}")
        return
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        click.echo(f"❌ Kutilmagan xatolik: {e}")
        return

    # Loadingni to‘xtatish
    stop_event.set()
    loading_thread.join()

    # Commit xabarini ko‘rsatish va amalni bajarish
    click.echo(f"✅ Generated commit message: {message}")
    if push:
        commit_and_push_git(message)
    else:
        commit_git(message)


cli.add_command(commit)

if __name__ == "__main__":
    cli()
