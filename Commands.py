import gc
import os


class Folder_Commands:
    def Navigate_To_Folder(Path: str) -> list[str | None]:
        # Returning The Items In A Folder
        return os.listdir(Path)
    
    def Make_A_Folder(Parent_Path: str, Name: str) -> str:
        Path_And_Name: str = os.path.join(Parent_Path, Name)
        # Making A Directory In the Given Path With The Given Name
        os.mkdir(Path_And_Name)
        
        return f" -- DIRECTORY MADE IN {Path_And_Name} -- "

    def Remove_A_Folder(Parent_Path: str, Name: str) -> str:
        Path_And_Name: str = os.path.join(Parent_Path, Name)
        # Removing The Directory In the Given Path With The Given Name
        os.rmdir(Path_And_Name)
        
        return f" -- DIRECTORY REMOVED IN {Path_And_Name} -- "


class File_Commands:
    def Make_A_File(Parent_Path: str, Name: str) -> str:
        Path_And_Name: str = os.path.join(Parent_Path, Name)
        # Making A File In the Given Path With The Given Name
        with open(f"{Path_And_Name}", "w+") as file:
            pass

        return f" -- FILE MADE IN {Path_And_Name} -- "

    def Remove_A_File(Parent_Path: str, Name: str) -> str:
        Path_And_Name: str = os.path.join(Parent_Path, Name)
        # Removing A File In the Given Path With The Given Name
        os.remove(Path_And_Name)

        return f" -- FILE REMOVED IN {Path_And_Name} -- "


class Searcher:
    def Search_Folder(Search_DIR: str, Folder: str) -> list[str | None]:
        results = []
        # Iterating Through The Files And Folders In The Head Directory
        for Root, Dir, File in os.walk(Search_DIR):
            if Folder in Root:
                Path_And_Name: str = str(os.path.join(Root, Folder))
                results.append(Path_And_Name)
        # Freeing Up The Ram To Prevent Memoery Leaks
        gc.collect()
        
        return results

    def Search_File(Search_DIR: str, file: str) -> list[str | None]:
        results = []
        # Iterating Through The Files And Folders In The Head Directory
        for Root, Dir, File in os.walk(Search_DIR):
            if file in File:
                Path_And_Name: str = str(os.path.join(Root, file))
                results.append(Path_And_Name)
        # Freeing Up The Ram To Prevent Memoery Leaks
        gc.collect()

        return results
