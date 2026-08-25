# CMPS 3603 Student Setup

## Part 1 — Create a GitHub Account and Configure Your Git Identity

GitHub will be used to distribute course materials and, later, to submit completed Jupyter notebooks. In this part, you will create and secure a GitHub account and configure the name and email address that Git records with your work.

You do **not** need a paid GitHub account for this course.

---

## What You Will Accomplish

By the end of this part, you should have:

- a personal GitHub account;
- a verified email address;
- a professional GitHub username;
- two-factor authentication and recovery codes;
- a configured Git author name and email, if Git is already installed; and
- a record of the GitHub username you will use for this course.

You will create the course repository in a later part.

---

# 1. Understand Git and GitHub

**Git** and **GitHub** are related, but they are not the same thing.

- **Git** is software on your computer that records versions of files.
- **GitHub** is a website that stores Git repositories and makes them available online.
- A **repository** is a project folder whose files and history are tracked by Git.
- A **commit** is a recorded checkpoint in that history.
- A **push** sends commits from your computer to GitHub.

You can make commits without being connected to the internet. Nothing becomes visible on GitHub until it is pushed.

For this course, you will commit your work locally as you progress and push it when instructed.

---

# 2. Create a Personal GitHub Account

If you already have a personal GitHub account, do not create another one. Sign in to your existing account and continue to the next section.

1. Visit [GitHub Signup](https://github.com/signup).
2. Follow the prompts to create a free personal account.
3. Use an email address you can access reliably.
4. Use a strong, unique password.
5. Complete the account-verification steps.

GitHub also permits signup through supported Google or Apple accounts. A regular email-and-password account is equally suitable for this course.

## Choose Your Username Carefully

Your GitHub username becomes part of the web address for every repository you own:

```text
https://github.com/your-username/repository-name
```

Choose a username you would be comfortable placing on a résumé, internship application, or professional portfolio.

Good examples:

```text
alex-smith
asmith42
jamie-data
```

Avoid usernames that are offensive, needlessly difficult to type, or likely to become embarrassing later.

Your GitHub username does **not** need to be your university username.

---

# 3. Verify Your Email Address

GitHub sends a verification message to the email address used during signup.

1. Open the verification email from GitHub.
2. Select the verification link.
3. Return to GitHub and confirm that the address is verified.

Without a verified email address, GitHub restricts basic activities such as creating repositories.

If the message does not appear:

- check the spam or junk folder;
- confirm that the address was entered correctly; and
- request another verification message from GitHub settings.

See [GitHub’s account-creation instructions](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github) if verification continues to fail.

---

# 4. Protect Your Account with Two-Factor Authentication

Two-factor authentication, commonly called **2FA**, requires a second form of verification in addition to your password.

1. Sign in to GitHub.
2. Open your profile menu in the upper-right corner.
3. Select **Settings**.
4. Select **Password and authentication**.
5. Follow GitHub’s instructions to enable two-factor authentication.

An authenticator application is generally preferable to relying only on text messages.

## Save Your Recovery Codes

When GitHub displays recovery codes:

1. download or print them;
2. store them somewhere secure; and
3. do not leave the only copy on the phone used for authentication.

Losing both your authenticator and your recovery codes can result in losing access to the account.

See [GitHub’s 2FA documentation](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa) for current setup and recovery instructions.

---

# 5. Decide Which Email Git Will Record

Every Git commit contains an author name and email address. Because your course repository will be public, consider whether you want your personal or university email address included in that public commit history.

You have two reasonable choices:

1. Use an email address verified on your GitHub account.
2. Use the private `noreply` email address provided by GitHub.

To locate GitHub’s private email option:

1. Open GitHub **Settings**.
2. Select **Emails**.
3. Review **Keep my email addresses private**.
4. Copy the GitHub-provided `noreply` address if you want to use it for commits.

The address may look similar to:

```text
12345678+your-username@users.noreply.github.com
```

Use the exact address displayed in your own GitHub settings. Do not copy the example above.

See [GitHub’s commit-email documentation](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) for more information.

---

# 6. Configure Your Git Author Name and Email

> Complete this section now if Git is already installed. If the `git` command is not found, return to this section immediately after installing Git in Part 2.

Open **Git Bash** on Windows or **Terminal** on macOS.

Set the name that should appear on your commits:

```bash
git config --global user.name "Your Name"
```

Set the email address that should appear on your commits:

```bash
git config --global user.email "your.email@example.com"
```

Replace the example values with your own information. Do not type `Your Name` or `your.email@example.com` literally.

For example:

```bash
git config --global user.name "Alex Smith"
git config --global user.email "12345678+alex-smith@users.noreply.github.com"
```

## Important Distinction

The value assigned to `user.name` is normally your human-readable name—not your GitHub username.

```text
GitHub username: alex-smith
Git author name: Alex Smith
```

The `--global` option applies these settings to repositories used by your computer account. You normally need to run these commands only once on each computer.

Git permanently records this information in new commits, so configure it before beginning course work. The official Git documentation describes this as part of the required [first-time Git setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

---

# 7. Verify Your Git Identity

Display the configured author name:

```bash
git config --global user.name
```

Display the configured email address:

```bash
git config --global user.email
```

Expected output will resemble:

```text
Alex Smith
12345678+alex-smith@users.noreply.github.com
```

You can also inspect the relevant configuration values together:

```bash
git config --global --list
```

If a value is incorrect, run its configuration command again with the correct information. The new value will replace the old one.

---

# 8. Record Your Course Account Information

Record the following information somewhere you can find it later:

```text
GitHub username:
GitHub profile URL:
Email used for Git commits:
Location of 2FA recovery codes:
```

Your profile URL should have this form:

```text
https://github.com/your-username
```

Do **not** record your GitHub password, authentication code, or recovery codes in a course repository or shared document.

You will later submit your GitHub username and course-repository URL through the class registration form.

---

# Completion Checklist

Before continuing to Part 2, confirm each item that applies:

- [ ] I have a personal GitHub account.
- [ ] My GitHub email address is verified.
- [ ] I know my exact GitHub username.
- [ ] I enabled two-factor authentication.
- [ ] I stored my recovery codes securely.
- [ ] I selected the email address Git should record in public commits.
- [ ] If Git is installed, I configured `user.name` and `user.email`.
- [ ] If Git is installed, I verified both configuration values.

Next: [**Part 2 — Install or Repair Git, Python, and Visual Studio Code**](./Part-02.md)
