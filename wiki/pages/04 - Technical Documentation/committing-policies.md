---
title: Committing policies
categories:
- Developers/General
- Developers/Tutorials
managed: false
source: wiki-scrape
wiki_revid: 109967
wiki_fetched_at: '2026-05-30T18:10:48Z'
---

## Contributing

### Create a bug report, feature request or GEP

- It is good practice for every change to have a bug report, feature request or [GEP (<strong>G</strong>ramps <strong>E</strong>nhancement <strong>P</strong>roposal''')](wiki:GEPS).
- Fixing a bug in an existing bug report is a good way to start Gramps development.

### Discuss the change on the mailing list

- Allows all developers to reach a consensus on a good design that conforms to our [developer policies](wiki:Developer_policies).
- Important for new features and changes to the user interface.
- Not necessary for small changes or when the has been sufficient discussion in the bug report.
- Agreeing to a design before coding could prevent wasted coding effort.
- If the change is large then you may be asked to write a GEP.

### Code the change

- Assign the bug report or feature request to yourself.
- Add the change to the [roadmap](wiki:{{man_version}}_Roadmap) if appropriate.
- Create a GEP branch for large changes.

### Create a pull request

- Unless it’s a trivial change, create a Pull Request (PR) to get your code reviewed.
- Add a link to the PR in the bug tracker. Use **p:gramps:nnn:** where nnn is the PR number.
- Regularly rebase your PR onto the upstream branch. Do not merge branches into your PR.

## Branches

- New features should be committed to the master branch.
- Only bug fixes should be committed to maintenance branches.
- The current maintenance branch should be merged regularly into the master branch.
- Translations may be committed to the *gramps* branch. Later versions use Weblate, and *po* files should not be modified directly.

## Merging

- Most changes should be squashed and fast-forwarded.
- Major new features should be merged no-ff to maintain their development identity.
- This applies both to pull requests and to work by developers with write permission to the repository.

## Pull requests

- Pull requests must be code-reviewed and tested by a developer.
- PR authors should not be assumed to be Git experts, so it's up to the Gramps developer doing the merge to ensure that the PR is clean and won’t make a mess of history.
- The GitHub "Squash and merge" button can be used for most small changes.
- A no-ff merge outside of GitHub should be used when it is useful to keep the commit history.
- Bug fixes must be committed to the current stable branch.
- Only new features should be committed to master directly.

## Log messages

Every commit to Git must be accompanied by a log message. These messages will be generated into a ChangeLog when a release is made and should conform to the following guidelines:

### Summary

- The first line of the commit message should consist of a short summary of the change.
- Maximum 70 characters.

### Description

- The description should be separated from the summary by a single blank line.
- Attempt to describe how the change affects the functionality from the user's perspective.
- Use complete sentences when possible.
- It is not necessary to describe minute details about the change nor the files that are affected because that information is already stored by Git and can be viewed with "git diff".
- When committing contributed code, the author should be credited using the --author option.
- If you want to refer to another commit, use the full commit hash. It will automatically be converted into a hyperlink by the GitHub web interface. Note: a 6 hexa digit hash enclosed in brackets WILL NOT WORK with GitHub auto-hyperlinking :-(

### Bug tracker integration

Special keywords can be used to either link to, or resolve, bug reports. They should be on the last line of the commit message separated by a single blank line.

To resolve a bug or bugs use:

- Fixes \#12345
- Fixed \#12345
- Resolves \#12345
- Resolved \#12345
- Fixes \#12345, \#67890
- Fixed \#12345, \#67890
- Resolves \#12345, \#67890
- Resolved \#12345, \#67890

To link to a bug or bugs use:

- Bug \#12345
- Issue \#12345
- Report \#12345
- Bugs \#12345, \#67890
- Issues \#12345, \#67890
- Reports \#12345, \#67890

For this to work, either the author or committer will need to be a developer on the Mantis bug tracker. The Git name must match either the Mantis username or real name, or the Git email must match the Mantis email.

### Useful commands

You can see the last changes with the git log command, an example usage of this command:

`git log --oneline`

You can also limit the number of entries shown by passing in the **-n** flag to git. Add **--stat** to see the files affected by the commit:

`git log -5`

To credit the contributor of a patch, use:

`git commit --author='A U Thor <author@example.com>'`

## Adding new files

All the files with the translatable strings **must** be listed in the `po/POTFILES.in` or `po/POTFILES.skip` files. This means that most new files must have their names added to these files.

Please remember to do this for new files that you add to Git.

### Check

You can make a test on a local copy:

`PYTHONPATH=../../gramps python po/test/po_test.py`

where ../.. is the path to your local copy

## Removing files

Remember to remove references to the file from the `po/POTFILES.in` and `po/POTFILES.skip` files.

## See also

- [Howto: Contribute to Gramps](wiki:Howto:_Contribute_to_Gramps)
- [How you can help](wiki:How_you_can_help)

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials)
