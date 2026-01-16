# Git Quick Reference

Use this cheat sheet to recall common Git workflows. Commands assume you are in the project directory you want to manage.

## Configure Your Identity (once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email you@example.com
```

## Initialize or Clone a Repository

- Start tracking an existing folder: `git init`
- Copy an existing repository: `git clone <url> [folder-name]`

## Inspect the Working Tree

- Check what changed: `git status`
- See unstaged changes: `git diff`
- See staged changes: `git diff --staged`

## Stage Files

- Add everything new or modified: `git add .`
- Stage a single file: `git add path/to/file`
- Unstage a file: `git restore --staged path/to/file`
- Remember that `git add` fills the staging area; only staged changes are captured by `git commit`, so you can curate what lands in each commit

## Commit Work

```bash
git commit -m "short, descriptive message"
```

- Amend the last commit (before pushing): `git commit --amend`
- Show history: `git log --oneline --graph`

## Branching Basics

- List branches (current one shows `*`): `git branch`
- Create and stay on a new branch: `git switch -c feature-name`
- Create a new branch from another branch (and check it out): `git switch -c juniorBranch test-branch`
- Switch to an existing branch: `git switch main`
- Rename the current branch: `git branch -m new-name` (if it tracked a remote branch, follow up with `git push origin -u new-name` and optionally remove the old remote ref via `git push origin --delete old-name`)

## Merging Workflow

1. Switch to the branch that should receive the changes (e.g., `main` or `juniorBranch`):
   ```bash
   git switch main
   ```
2. Update it if needed (e.g., `git pull` if you have remotes).
3. Merge another branch, such as `test-branch`:
   ```bash
   git merge test-branch
   ```
4. Resolve any conflicts, stage the fixes, and finish with `git commit`.

- Abort an in-progress merge before committing: `git merge --abort`
- Remember the direction: the branch you currently have checked out receives changes from the branch named in `git merge other-branch`

## Deleting Branches

- Remove a branch that has already been merged: `git branch -d test-branch`
- Force-delete an unmerged branch (only if you are sure): `git branch -D test-branch`

## Stashing (optional but handy)

- Save uncommitted work temporarily: `git stash push -m "message"`
- Reapply later: `git stash pop`

## Useful Clean-Up Commands

- Restore a file to the last committed version: `git restore --source=HEAD --worktree path/to/file`
- Discard all local changes (dangerous!): `git reset --hard HEAD`
- Make a file match another branch without merging everything: `git restore --source=other-branch --staged --worktree path/to/file` (then commit)

## Working With GitHub (or Any Remote)

- Add a remote after creating a repo on GitHub: `git remote add origin git@github.com:username/project.git`
- Push your local `main` the first time (and set upstream): `git push -u origin main`
- Remember: `git add` and `git commit` only update your local repository—run `git push` once commits are ready to publish
- Pull updates from GitHub: `git pull` (pulls from the upstream branch)
- Push new commits on any branch: `git push`
- Publish a new branch: `git push -u origin feature-name`
- After the initial `-u` push, you can just run `git push`/`git pull` while on that branch and Git will target the tracked remote branch automatically
- Delete a remote branch: `git push origin --delete feature-name`
- See remote refs: `git remote -v` and `git branch -r`
- Public repos are readable by anyone; private repos require you to authenticate (HTTPS token or SSH key associated with your GitHub account) before you can clone or push
- Even on public/open-source repos, only collaborators with write access (or maintainers merging pull requests) can push updates—others must fork and open PRs
- `origin` is just the conventional name for the first remote; add more remotes with custom labels (e.g., `git remote add mysecond https://github.com/user/AnotherRepo.git`) and push/pull from each explicitly (`git push mysecond main`)

## Deploying to Heroku

- Install the Heroku CLI and log in: `heroku login`
- Attach your local repo to an app: `heroku git:remote -a your-app-name`
- Keep GitHub (`origin`) as the collaboration remote; Heroku is a separate remote (normally named `heroku`)
- Deploy by pushing the branch you want to run: `git push heroku main` (or any branch you target)
- Each push to the Heroku remote triggers a build/deploy; it doesn’t replace your GitHub history

Keep this file nearby when working in Git so you can follow the common sequence: initialize → edit → stage → commit → branch → merge → clean up.
