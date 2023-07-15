import time
import os

def set_frames():
    frames = []

    frames.append('''
                    ##         .
                ## ## ##        ==
            ## ## ## ## ##    ===
        /\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
        \______ o           __/
            \    \         __/
            \____\_______/
    ''')

    frames.append('''
                    ##         .
                ## ## ##        ==
            ## ## ## ## ##    ===
        /\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ /  ===- ~~~
        \______ o           __/
            \    \         __/
            \____\_______/
    ''')

    return frames

if __name__ == "__main__":
    frames = set_frames()    

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for frame in frames:
            print(frame)
            time.sleep(0.2)
            os.system('cls' if os.name == 'nt' else 'clear')
