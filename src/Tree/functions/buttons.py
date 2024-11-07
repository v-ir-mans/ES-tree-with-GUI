import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

def open_file_dialog(parent, file_type="CSV Files (*.csv);;All Files (*)"):
    """
    Opens a file dialog and returns the selected file path.
    
    Args:
        parent: The parent widget.
        file_type: The file type filter (e.g., "CSV Files (*.csv);;Text Files (*.txt)").
    
    Returns:
        The file path if a file is selected, False otherwise.
    """

    options = QFileDialog.Options()
    file_name, _ = QFileDialog.getOpenFileName(parent, "Open File", "", file_type, options=options)

    if _:
        return file_name
    else:
        return False

def save_file_dialog(parent, extension="csv", file_type="CSV Files (*.csv);;All Files (*)", default_name="untitled" ):
    """
    Opens a file dialog to save a file and returns the file path.

    Args:
        parent: The parent widget.
        default_name: Default file name to display in the dialog.
        extension: Default file extension to use if the user does not specify.
        file_type: The file type filter for saving files (e.g., "CSV Files (*.csv);;Text Files (*.txt)").

    Returns:
        The file path where the user wants to save the file, False otherwise.
    """
    
    options = QFileDialog.Options()
    file_name, _ = QFileDialog.getSaveFileName(parent, "Save File", f"{default_name}.{extension}", file_type, options=options)

    # Add default extension if not provided by the user
    if file_name and not file_name.endswith(f".{extension}"):
        file_name += f".{extension}"

    if _:
        return file_name
    else:
        return False
