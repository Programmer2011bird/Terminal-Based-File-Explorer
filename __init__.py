import Commands

print(""" 
       --- Terminal Based File Explorer ---
      
       -- Press Ctrl+C or Type exit to quit -- 
       -- Type NavF to Navigate to a folder -- 
       -- Type MkDIR to Make a Folder -- 
       -- Type RmDIR to Remove a Folder -- 
       -- Type MkFi to Make a File -- 
       -- Type RmFi to Remove a File -- 
       -- Type SeaDIR to Search For a Folder -- 
       -- Type SeaFi to Search For a File -- """)

RUNNING: bool = True

while RUNNING:
    try:
        COMMAND: str = str(input(">> "))
    
        if COMMAND == "exit":
            RUNNING = False
            print(" -- Exited -- ")
        
        match COMMAND:
            case "NavF":
                FOLDER_PATH: str = str(input("Folder's Path >> "))
                OUTPUT: list[str] = Commands.Folder_Commands.Navigate_To_Folder(f"{FOLDER_PATH}")

                for _, item in enumerate(OUTPUT):
                    print(item)
            
            case "MkDIR":
                PARENT_FOLDER: str = str(input("Parent Folder's Path >> "))
                NAME: str = str(input("Folder's Name >> "))

                print(Commands.Folder_Commands.Make_A_Folder(PARENT_FOLDER, NAME))
            
            case "MkFi":
                PARENT_FOLDER: str = str(input("Parent Folder's Path >> "))
                NAME: str = str(input("Files's Name >> "))

                print(Commands.File_Commands.Make_A_File(PARENT_FOLDER, NAME))

            case "RmDIR":
                PARENT_FOLDER: str = str(input("Parent Folder's Path >> "))
                NAME: str = str(input("Folder's Name >> "))

                print(Commands.Folder_Commands.Remove_A_Folder(PARENT_FOLDER, NAME))
            
            case "RmFi":
                PARENT_FOLDER: str = str(input("Parent Folder's Path >> "))
                NAME: str = str(input("File's Name >> "))

                print(Commands.File_Commands.Remove_A_File(PARENT_FOLDER, NAME))
            
            case "SeaDIR":
                HEAD_DIR: str = str(input("Head Directory >> "))
                NAME: str = str(input("Folder's Name >> "))

                OUTPUT: list[str | None] = Commands.Searcher.Search_Folder(HEAD_DIR, NAME)

                for _, item in enumerate(OUTPUT):
                    print(f"-- {item}")

            case "SeaFi":
                HEAD_DIR: str = str(input("Head Directory >> "))
                NAME: str = str(input("File's Name >> "))

                OUTPUT: list[str | None] = Commands.Searcher.Search_File(HEAD_DIR, NAME)

                for _, item in enumerate(OUTPUT):
                    print(f"-- {item}")

    except KeyboardInterrupt:
        print(" -- Exited -- ")
        RUNNING = False