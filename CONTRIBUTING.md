# Contributing to Pluto

Want to contribute to Pluto? Yay! We're always happy to have more contributors. Before you start developing, though, we ask that you read through this document in-full. It's full of tips and guidelines--if you skip it, you'll likely miss something important (and your pull request will probably be rejected as a result).

Throughout the process of contributing, there's one thing we'd like you to remember: Pluto was developed (and is maintained) by what might be described as "volunteers". They earn no money for their work on Pluto and give their time solely for the advancement of the software and the enjoyment of its users. While they will do their best to get back to you regarding issues and pull requests, **your patience is appreciated**.

## Reporting Bugs

The [bug tracker](https://github.com/C-O-S-T-A-JDM/Pluto-client/issues) at Github is for reporting bugs in Pluto.

If you think that you found a bug and that you're using the most recent version of Pluto, please include a detailed description what you did and how to reproduce the bug. If Pluto crashes, run it with `--debug` as command line argument and also include the full stacktrace (not just the last line). If you post output, put it into a [fenced code block](https://help.github.com/articles/github-flavored-markdown/#fenced-code-blocks). Last but not least: have a look at [Simon Tatham's "How to Report Bugs Effectively"](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html) to learn how to write a good bug report.

## Opening Pull Requests
You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.
### Philosophies

There are a few key philosophies to preserve while designing features for Pluto:

1. **The core Pluto software (`Pluto-client`) must remain decoupled from any third-party web services.** For example, the Pluto core should never depend on Google Translate in any way. This is to avoid unnecessary dependences on web services that might change or become paid over time.
2. **The core Pluto software (`Pluto-client`) must remain decoupled from any paid software or services.** Of course, you're free to use whatever you'd like when running Pluto locally or in a fork, but the main branch needs to remain free and open-source.
3. **Pluto should be _usable_ by both beginner and expert programmers.** If you make a radical change, in particular one that requires some sort of setup, try to offer an easy-to-run alternative or tutorial. See, for example, the profile populator ([`jasper-client/client/populate.py`](https://github.com/jasperproject/jasper-client/blob/master/client/populate.py)), which abstracts away the difficulty of correctly formatting and populating the user profile.

### DOs and DON'Ts

While developing, you **_should_**:


1. **Ensure that the existing unit tests pass.** They can be run via `python2 -m unittest discover` for Pluto's main folder.
2. **Test _every commit_ on a Raspberry Pi**. Testing locally (i.e., on OS X or Windows or whatnot) is insufficient, as you'll often run into semi-unpredictable issues when you port over to the Pi. You should both run the unit tests described above and do some anecdotal testing (i.e., run Pluto, trigger at least one module).
3. **Include docstrings that follow our existing format!** Good documentation is a good thing.
4. **Add any new Python dependencies to requirements.txt.** Make sure that your additional dependencies are dependencies of `Pluto-client` and not existing packages on your disk image!
5. **Explain _why_ your change is necessary.** What does it accomplish? Is this something that others will want as well?

Thank you for following these guidlines when contributing to Pluto.
Happy coding!
