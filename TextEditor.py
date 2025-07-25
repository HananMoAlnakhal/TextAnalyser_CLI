import msvcrt
import os
from predictor import *
from lang_models import *
from TEXTstyling import *
# Simple undo/redo stack
undo_stack = []
redo_stack = []

def save_state(text, pos):
    """Save current state for undo"""
    global undo_stack, redo_stack
    undo_stack.append((text, pos))
    if len(undo_stack) > 20:  # Keep last 20 states
        undo_stack.pop(0)
    redo_stack.clear()

def undo():
    """Undo last action"""
    global undo_stack, redo_stack
    if len(undo_stack) > 1:
        current = undo_stack.pop()
        redo_stack.append(current)
        return undo_stack[-1]
    return None

def redo():
    """Redo last undone action"""
    global undo_stack, redo_stack
    if redo_stack:
        state = redo_stack.pop()
        undo_stack.append(state)
        return state
    return None

def clear_screen():
    os.system('cls')

def get_key():
    first = msvcrt.getch()
    if first == b'\x00' or first == b'\xe0':
        second = msvcrt.getch()
        if second == b'H':
            return 'UP'
        elif second == b'P':
            return 'DOWN'
        elif second == b'K':
            return 'LEFT'
        elif second == b'M':
            return 'RIGHT'
        elif second == b'G':
            return 'HOME'
        elif second == b'O':
            return 'END'
        elif second == b'S':
            return 'DELETE'
    elif first == b'\x1a':  # Ctrl+Z
        return 'CTRL_Z'
    elif first == b'\x19':  # Ctrl+Y
        return 'CTRL_Y'
    elif first == b'\r':
        return 'ENTER'
    elif first == b'\t':
        return 'SELECT'
    elif first == b'\b':
        return 'BACKSPACE'
    elif first == b' ':
        return 'SPACE'
    elif first == b'\x1b':  # ESC
        return 'ESC'
    
    return first.decode(errors='ignore')

def writing_line(p=0):
    def print_Text(noPointer=False):
        print(f'\033[{p};0H'+" "*100)
        if not noPointer:
            print(f'\033[{p};0H'+"> "+text[:pos]+"|"+text[pos:])
            # Clear suggestion lines
            for i in range(1,4):
                print(f'\033[{p+i};0H'+" "*100)
            # Print suggestions
            if GetNext and NextWords:
                for ind, Word in enumerate(NextWords[:3]):
                    print(f'\033[{p+ind+1};0H'+" "*100)
                    if ind == selected_suggestion:
                        # Highlight selected suggestion in green
                        print(f'\033[{p+ind+1};0H ',text+"\33[38;5;10m"+Word[0]+"\33[0m")
                    else:
                        print(f'\033[{p+ind+1};0H ',text+"\33[38;5;31m"+Word[0]+"\33[0m")
            elif not GetNext and CurrentWords:
                for ind, Word in enumerate(CurrentWords[:3]):
                    print(f'\033[{p+ind+1};0H'+" "*100)
                    base_text = text[:-len(Last_part)] if Last_part else text
                    if ind == selected_suggestion:
                        # Highlight selected suggestion in green
                        print(f'\033[{p+ind+1};0H ',base_text+"\33[38;5;10m"+Word[0]+"\33[0m")
                    else:
                        print(f'\033[{p+ind+1};0H ',base_text+"\33[38;5;31m"+Word[0]+"\33[0m")
        else:
            print(f'\033[{p};0H'+"> "+text)
    
    text = ""
    pos = 0
    GetNext = False
    last2Words = []
    Last_part = ""
    CurrentWords = []
    NextWords = []
    selected_suggestion = 0  # Track which suggestion is selected
    
    # Save initial state
    save_state(text, pos)
    
    print_Text()

    while True:
        if msvcrt.kbhit():
            CHAR = get_key()
            
            if CHAR == 'ENTER':
                print_Text(noPointer=True)
                break
            
            elif CHAR == 'CTRL_Z':
                # Undo
                state = undo()
                if state:
                    text, pos = state
                    selected_suggestion = 0  # Reset selection
                    # Update predictions after undo
                    words = text.split()
                    if words:
                        Last_part = words[-1]
                        last2Words = words[-2:] if len(words) >= 2 else words
                        if text.endswith(' '):
                            GetNext = True
                            try:
                                if len(last2Words) >= 2:
                                    # Use 3-gram when we have 2 or more words
                                    NextWords = Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                                else:
                                    # Use 2-gram when we have only 1 word
                                    NextWords = Pred2Gram.predict_next_top(" ".join(last2Words))[:3]
                            except:
                                NextWords = []
                        else:
                            GetNext = False
                            try:
                                predictions = Pred2Gram.predict_next_top(" ".join(last2Words[:-1]) if len(last2Words) > 1 else "")
                                CurrentWords = [w for w in predictions if w[0].startswith(Last_part)][:3]
                                # If n-gram doesn't provide enough results, use Trie as fallback
                                if len(CurrentWords) < 3:
                                    try:
                                        trie_completions = TRIE.auto_complete(Last_part)
                                        trie_words = [(comp, 1.0) for comp in trie_completions if comp not in [w[0] for w in CurrentWords]]
                                        CurrentWords.extend(trie_words[:3-len(CurrentWords)])
                                    except:
                                        pass
                            except:
                                # If n-gram fails completely, try Trie
                                try:
                                    trie_completions = TRIE.auto_complete(Last_part)
                                    CurrentWords = [(comp, 1.0) for comp in trie_completions[:3]]
                                except:
                                    CurrentWords = []
                    else:
                        Last_part = ""
                        CurrentWords = []
                        NextWords = []
                        GetNext = False
                print_Text()
                continue
                
            elif CHAR == 'CTRL_Y':
                # Redo
                state = redo()
                if state:
                    text, pos = state
                    selected_suggestion = 0  # Reset selection
                    # Update predictions after redo
                    words = text.split()
                    if words:
                        Last_part = words[-1]
                        last2Words = words[-2:] if len(words) >= 2 else words
                        if text.endswith(' '):
                            GetNext = True
                            try:
                                if len(last2Words) >= 2:
                                    # Use 3-gram when we have 2 or more words
                                    NextWords = Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                                else:
                                    # Use 2-gram when we have only 1 word
                                    NextWords = Pred2Gram.predict_next_top(" ".join(last2Words))[:3]
                            except:
                                NextWords = []
                        else:
                            GetNext = False
                            try:
                                predictions = Pred2Gram.predict_next_top(" ".join(last2Words[:-1]) if len(last2Words) > 1 else "")
                                CurrentWords = [w for w in predictions if w[0].startswith(Last_part)][:3]
                                # If n-gram doesn't provide enough results, use Trie as fallback
                                if len(CurrentWords) < 3:
                                    try:
                                        trie_completions = TRIE.auto_complete(Last_part)
                                        trie_words = [(comp, 1.0) for comp in trie_completions if comp not in [w[0] for w in CurrentWords]]
                                        CurrentWords.extend(trie_words[:3-len(CurrentWords)])
                                    except:
                                        pass
                            except:
                                # If n-gram fails completely, try Trie
                                try:
                                    trie_completions = TRIE.auto_complete(Last_part)
                                    CurrentWords = [(comp, 1.0) for comp in trie_completions[:3]]
                                except:
                                    CurrentWords = []
                    else:
                        Last_part = ""
                        CurrentWords = []
                        NextWords = []
                        GetNext = False
                print_Text()
                continue

            elif CHAR == "LEFT":
                if pos > 0:
                    pos -= 1
                print_Text()

            elif CHAR == "RIGHT":
                if pos < len(text):
                    pos += 1
                print_Text()
                
            elif CHAR == "HOME":
                pos = 0
                print_Text()
                
            elif CHAR == "END":
                pos = len(text)
                print_Text()
                
            elif CHAR == "DELETE":
                if pos < len(text):
                    save_state(text, pos)
                    text = text[:pos] + text[pos+1:]
                    selected_suggestion = 0  # Reset selection
                    # Update predictions
                    words = text.split()
                    if words and not text.endswith(' '):
                        Last_part = words[-1]
                        GetNext = False
                        try:
                            predictions = Pred2Gram.predict_next_top(" ".join(words[:-1]) if len(words) > 1 else "")
                            CurrentWords = [w for w in predictions if w[0].startswith(Last_part)][:3]
                        except:
                            CurrentWords = []
                    print_Text()

            elif CHAR == "SELECT":
                if GetNext and NextWords and selected_suggestion < len(NextWords):
                    save_state(text, pos)
                    selected_word = NextWords[selected_suggestion][0]
                    text += selected_word + " "
                    pos += len(selected_word) + 1
                    
                    # After adding the word, get suggestions for the next word
                    GetNext = True
                    words = text.split()
                    last2Words = words[-2:] if len(words) >= 2 else words
                    try:
                        if len(last2Words) >= 2:
                            # Use 3-gram when we have 2 or more words
                            NextWords = Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                        else:
                            # Use 2-gram when we have only 1 word
                            NextWords = Pred2Gram.predict_next_top(" ".join(last2Words))[:3]
                    except:
                        NextWords = []
                    selected_suggestion = 0  # Reset selection
                    
                elif not GetNext and CurrentWords and selected_suggestion < len(CurrentWords):
                    save_state(text, pos)
                    selected_word = CurrentWords[selected_suggestion][0]
                    text = text[:-len(Last_part)] + selected_word + " "
                    pos += len(selected_word) - len(Last_part) + 1
                    
                    # After completing the word, get suggestions for the next word
                    GetNext = True
                    words = text.split()
                    last2Words = words[-2:] if len(words) >= 2 else words
                    try:
                        if len(last2Words) >= 2:
                            # Use 3-gram when we have 2 or more words
                            NextWords = Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                        else:
                            # Use 2-gram when we have only 1 word
                            NextWords = Pred2Gram.predict_next_top(" ".join(last2Words))[:3]
                    except:
                        NextWords = []
                    CurrentWords = []
                    selected_suggestion = 0  # Reset selection
                    
                print_Text()
                
            elif CHAR == "UP":
                # Navigate up in suggestions
                if GetNext and NextWords:
                    selected_suggestion = (selected_suggestion - 1) % len(NextWords)
                    print_Text()
                elif not GetNext and CurrentWords:
                    selected_suggestion = (selected_suggestion - 1) % len(CurrentWords)
                    print_Text()
                
            elif CHAR == "DOWN":
                # Navigate down in suggestions
                if GetNext and NextWords:
                    selected_suggestion = (selected_suggestion + 1) % len(NextWords)
                    print_Text()
                elif not GetNext and CurrentWords:
                    selected_suggestion = (selected_suggestion + 1) % len(CurrentWords)
                    print_Text()
                
            elif CHAR == "ESC":
                break
                
            else:
                save_state(text, pos)
                
                if CHAR == "SPACE":
                    CHAR = " "
                    GetNext = True
                    selected_suggestion = 0  # Reset selection
                    words = text.split()
                    last2Words = words[-2:] if len(words) >= 2 else words
                    try:
                        NextWords = Pred3Gram.predict_next_top(" ".join(last2Words))[:3]
                    except:
                        NextWords = []
                    text = text[:pos] + CHAR + text[pos:]
                    pos += 1

                elif CHAR == "BACKSPACE":
                    if pos > 0:
                        if text[pos-1] == " ":
                            GetNext = False
                        text = text[:pos-1] + text[pos:]
                        pos -= 1
                        selected_suggestion = 0  # Reset selection
                        # Update predictions
                        words = text.split()
                        if words and not text.endswith(' '):
                            Last_part = words[-1]
                            try:
                                predictions = Pred2Gram.predict_next_top(" ".join(words[:-1]) if len(words) > 1 else "")
                                CurrentWords = [w for w in predictions if w[0].startswith(Last_part)][:3]
                                # If n-gram doesn't provide enough results, use Trie as fallback
                                if len(CurrentWords) < 3:
                                    try:
                                        trie_completions = TRIE.auto_complete(Last_part)
                                        trie_words = [(comp, 1.0) for comp in trie_completions if comp not in [w[0] for w in CurrentWords]]
                                        CurrentWords.extend(trie_words[:3-len(CurrentWords)])
                                    except:
                                        pass
                            except:
                                # If n-gram fails completely, try Trie
                                try:
                                    trie_completions = TRIE.auto_complete(Last_part)
                                    CurrentWords = [(comp, 1.0) for comp in trie_completions[:3]]
                                except:
                                    CurrentWords = []
                        else:
                            Last_part = ""
                            CurrentWords = []

                elif len(CHAR) == 1 and CHAR.isprintable():
                    GetNext = False
                    selected_suggestion = 0  # Reset selection
                    text = text[:pos] + CHAR + text[pos:]
                    words = text.split()
                    Last_part = words[-1] if words and not text.endswith(' ') else ""
                    last2Words = words[-2:] if len(words) >= 2 else words
                    
                    if Last_part:
                        try:
                            predictions = Pred2Gram.predict_next_top(" ".join(last2Words[:-1]) if len(last2Words) > 1 else "")
                            CurrentWords = [w for w in predictions if w[0].startswith(Last_part)][:3]
                            # If n-gram doesn't provide enough results, use Trie as fallback
                            if len(CurrentWords) < 3:
                                try:
                                    trie_completions = TRIE.auto_complete(Last_part)
                                    # Convert trie results to same format as n-gram results
                                    trie_words = [(comp, 1.0) for comp in trie_completions if comp not in [w[0] for w in CurrentWords]]
                                    CurrentWords.extend(trie_words[:3-len(CurrentWords)])
                                except:
                                    pass
                        except:
                            # If n-gram fails completely, try Trie
                            try:
                                trie_completions = TRIE.auto_complete(Last_part)
                                CurrentWords = [(comp, 1.0) for comp in trie_completions[:3]]
                            except:
                                CurrentWords = []
                    else:
                        CurrentWords = []
                    pos += 1
                    
                print_Text()

    return text

def SmartTextEditor(stopCriteria="#"):
    lines = []
    x = ""
    pointer_pos = 1
    clear_screen()
    
    # Print simple header
    print(f'Smart Text Editor - Press {SkyBlue("ESC / ENTER")} to go to next line, {SkyBlue("Ctrl+Z")} to undo, {SkyBlue("Ctrl+Y")} to redo, Use {SkyBlue("UP/DOWN arrows")} to navigate suggestions, {SkyBlue("TAB")} to select one')
    print(f"when done add a final line with {FOSHII(stopCriteria)} and press enter")
    print("="*60)
    
    while True:
        x = writing_line(p=pointer_pos+2)
        if x.startswith(stopCriteria):
            break
        if x!="":
            lines.append(x.lower().strip())
        pointer_pos += 1
    if lines==[]:
        clear_screen()
        print(CENTER_SCREEN(BOLD("You entered NO text to be processed please enter again or press E to hose another way of entering")))
        return SmartTextEditor()
    return lines

if __name__ == "__main__":
    print(SmartTextEditor())