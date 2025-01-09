---

# **Git Auto Uploader**

Git Auto Uploader is a Python-based desktop application that simplifies uploading and publishing local project folders to GitHub as open-source repositories. Using a graphical user interface (GUI), users can select a project folder, provide a repository name, and automate the process of pushing the code to GitHub.

---

## **Features**

- Easy-to-use **Tkinter GUI**.
- Create new repositories on GitHub automatically.
- Upload selected project folders from your local machine.
- Initialize Git, add files, commit, and push to the GitHub repository.
- Notifications upon successful repository creation and push.

---

## **Requirements**

- Python 3.7 or higher.
- A GitHub account.
- Git installed on your system.
- A GitHub Personal Access Token (PAT) with repository permissions.

---

## **Setup and Installation**

1. **Clone or Download the Project**  
   Download or clone this repository:
   ```bash
   git clone https://github.com/TusharFodse/GitAutoUploader
   cd GitAutoUploader
   ```


2. **Set Up Environment Variable**  
   Set up your GitHub Personal Access Token (PAT) as an environment variable:
   - **On Windows**:
     ```bash
     set GITHUB_TOKEN=your_personal_access_token
     ```
   - **On Linux/Mac**:
     ```bash
     export GITHUB_TOKEN=your_personal_access_token
     ```

   > **Note**: Ensure your PAT has `repo` scope for creating and managing repositories.

4. **Run the Application**  
   Launch the application:
   ```bash
   python gitpipline.py
   ```

---

## **How to Use**

1. Enter the desired **repository name** in the input field.
2. Click on the **"Open Git"** button to select the folder you want to upload.
3. The application will:
   - Create a new repository on GitHub.
   - Initialize Git in the selected folder.
   - Add, commit, and push the files to the new repository.
4. A notification will confirm the successful upload.
## Note:-If Notification is not Show but console Print Repositry created then Repositry create
---

## **Technologies Used**

- **Python**: Core scripting.
- **Tkinter**: For GUI design.
- **Git**: Version control.
- **GitHub API**: To create and manage repositories.
- **Plyer**: For desktop notifications.

---

## **Known Issues**

- Ensure no sensitive data (like tokens) is hardcoded in your script, as GitHub push protection may block the upload.
- Ensure Git is installed and configured on your system.

---

## **Future Enhancements**

- Add support for private repositories.
- Provide an option to manage multiple GitHub accounts.
- Include progress indicators for file uploads.

---

## **Contributing**

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.  

---



### **Main Interface:**
![Main Interface](https://via.placeholder.com/600x400.png?text=Main+Interface)

---

Let me know if you'd like to add more sections!
