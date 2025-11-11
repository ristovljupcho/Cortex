# 🎯 Discord Role & Member Management Bot  

A **Discord bot** built with `discord.py` that automates **member management**, **welcome messages**, and **reaction-role polls**.  
This bot provides seamless onboarding for new members and enables self-assignable roles through emoji reactions.

---

## 🚀 Features  

### 👋 Member Management  
- Sends a **welcome message** when a new member joins.  
- Sends a **farewell message** when a member leaves.  
- Automatically assigns **predefined roles** (e.g., “Member”, “DJ”) to new members.  
- Optionally sends a **direct message (DM)** to greet new users personally.  

### 🗳️ Reaction Role Polls  
- Create **role polls** that allow members to assign roles to themselves by reacting with emojis.  
- Admins can easily add or remove role-emoji mappings with simple commands.  
- Real-time role assignment/removal when a user adds or removes a reaction.  

---

## 🧩 Commands  

| Command | Description | Permission Required |
|----------|--------------|---------------------|
| `!create_poll` | Create a new reaction-role poll embed. | Manage Roles |
| `!add_poll_role <emoji> <role>` | Add a role option to the poll. | Manage Roles |
| `!remove_poll_role <emoji>` | Remove a role option from the poll. | Manage Roles |

---

## ⚙️ Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Install Dependencies  
Make sure you have Python **3.10+** installed.  
Then run:
```bash
pip install -U discord.py python-dotenv
```

### 3️⃣ Configure Environment Variables  
Create a `.env` file in the project root and add your Discord bot token:
```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4️⃣ Set Up Folder Structure  
Make sure your project has this structure:
```
.
├── cogs/
│   ├── member_management.py
│   └── role_poll_management.py
├── main.py
├── .env
└── README.md
```

---

## 🧠 Code Overview  

### 🧩 `cogs/member_management.py`
Handles:
- Welcome/farewell messages  
- Role assignment for new members  

### 🧩 `cogs/role_poll_management.py`
Handles:
- Reaction-role polls  
- Emoji → Role mapping management  
- Reaction event listeners  

### 🧩 `main.py`
Handles:
- Bot startup  
- Cog loading  
- Logging configuration  

---

## 🔒 Permissions  

When adding the bot to your server, make sure it has the following permissions:
- `Manage Roles`
- `Send Messages`
- `Add Reactions`
- `Read Message History`
- `Manage Messages` (for removing invalid reactions)
- `View Channels`

---

## 🪄 Example Usage  

**1.** Admin runs:  
```
!create_poll
```

**2.** Then adds some roles:  
```
!add_poll_role 🎮 Gamer
!add_poll_role 🎵 Musician
```

**3.** Members react with 🎮 or 🎵 to self-assign roles.  
Removing their reaction removes the role automatically.

---

## 🧰 Technologies Used  
- [Python 3.10+](https://www.python.org/downloads/)  
- [discord.py](https://github.com/Rapptz/discord.py)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 🧾 Logging  

All runtime logs are saved in `discord.log` for easier debugging.  

---

## 🤝 Contributing  

Contributions are welcome!  
Feel free to fork this repo, open issues, or submit pull requests.

---

## 🧑‍💻 Author  

**Developed by:** [Your Name](https://github.com/<your-username>)  
💬 Feel free to reach out for feature suggestions or improvements!  

---

## 🪙 License  

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🧩 Potential Add-ons  

Here are some ideas for expanding this bot’s functionality in the future:  

- 🕵️‍♂️ **Verification System:** Require new users to react to a message before gaining access.  
- 🧠 **Custom Welcome Embed Builder:** Allow admins to design embeds for welcome messages.  
- 🏷️ **Dynamic Role Categories:** Group roles by type (e.g., Game Roles, Interest Roles).  
- 🔄 **Persistent Role Polls:** Store reaction-role data in a database (SQLite, PostgreSQL) so it persists after restarts.  
- 📈 **Activity Tracking:** Assign badges or ranks based on user activity.  
- 🧹 **Auto Cleanup:** Remove unused roles or polls automatically.  
- ⏰ **Scheduled Announcements:** Add a timed message scheduler for server updates or events.  
- 🎫 **Support Ticket System:** Allow members to open support tickets in private channels.  
- 🗂️ **Cog Auto-Loader:** Automatically detect and load new cogs on startup.  

---

## 📝 TODO  

- [ ] Add database persistence for roles and reaction mappings.  
- [ ] Implement a command for setting custom welcome/farewell messages.  
- [ ] Improve error handling and logging.  
- [ ] Add admin command to reload or disable cogs dynamically.  
- [ ] Add emoji validation to prevent using invalid emoji.  
- [ ] Create a web dashboard for bot configuration.  
- [ ] Add command usage help embeds (`!help`).  
- [ ] Add localization (multi-language support).  
- [ ] Add bot statistics (total members joined, roles assigned, etc.).  
- [ ] Dockerize the bot for easier deployment.  
