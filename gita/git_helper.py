import git


def get_repo():
    return git.Repo(".")


def get_diff():
    repo = get_repo()
    return repo.git.diff()


def commit_git(message):
    repo = get_repo()
    repo.git.add(A=True)
    repo.index.commit(message)
    print(f"✅ AI commit yaratildi va push qilindi:\n\n{message}")


def commit_and_push_git(message):
    repo = get_repo()
    commit_git(message)
    repo.remote(name="origin")
    print("✅ O'zgarishlar GitHub'ga push qilindi.")
