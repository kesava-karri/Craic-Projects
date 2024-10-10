### Use case/Backstory:

- Yes, I believe in all the repetitive tasks should be scripted/automated :). since git actions are something we perform almost everyday, I had to come up with this script.

### Description/Walk-through:

- Copy the file to respective git repo
- Run the script using
  `./automateGit.sh -m "COMMIT_MESSAGE_HERE"`
  or
  [To have a specific date of commit]
  `./automateGit.sh --date "2023-11-10" -m "COMMIT_MESSAGE_HERE"`
- Steps it follows:
  ```
  git add .
  git commit -m "GIVEN_COMMIT_MESSAGE_HERE"
  git push origin main
  ```
