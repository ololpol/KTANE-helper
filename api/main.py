import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware  
import json
import re

#uvicorn main:app --reload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.options('/api/apitest')
async def options_test():
    return {}

@app.get('/api')
async def root(): 
    return {"message":"Hi there"}

@app.post('/api/apitest')
async def test(payload: dict = Body(...)):
    print(payload)
    if "p1" in payload.keys() and "p2" in payload.keys():
        out = payload["p1"] + " fromAPI " + payload["p2"]
        return {"value": out}

@app.post("/api/wires")
async def wires(payload: dict= Body(...)):
    wires : str = payload["p1"]
    state = json.load(open("bombState.json","r"))
    last = int(state["serial"][-1]) % 2 == 1
    options: list(function(str, bool)) = []
    if len(wires) == 3:
        options = [
            (lambda x, y:2 if not("r" in x) else 0),
            (lambda x, y:3 if x[-1] == "w" else 0),
            (lambda x, y:(x.index("u", x.index("u")+1)+1)
                        if (x.count("u")>1) else 0),
            (lambda x, y: 3)
        ]
    if len(wires) == 4:
        options = [
            lambda x, y:(x.index("r", x.index("r")+1)+1)
                        if ((x.count("r")>1) and y) else 0,
            lambda x, y:(1 if x[-1] == "y" and (not "r" in x) else 0),
            lambda x, y:(1 if x.count("u") == 1 else 0),
            lambda x, y:(4 if x.count("y") > 1 else 0),
            lambda x, y: 2
        ]
    if len(wires) == 5:
        options = [
            lambda x, y:(4 if x[-1] == "b" and y else 0),
            lambda x, y:(1 if x.count("r") == 1 and x.count("u") > 1 else 0),
            lambda x, y:(2 if x.count("b") == 2 else 0),
            lambda x, y:1
        ]
    if len(wires) == 6:
        options = [
            lambda x, y:(3 if x.count("u") == 0 and y else 0),
            lambda x, y:(4 if x.count("y") == 1 and x.count("w") > 1 else 0),
            lambda x, y:(6 if x.count("r") == 0 else 0),
            lambda x, y:4
        ]
    for option in options:
        if option(wires, last) != 0:
            return {"value": option(wires, last)}

#P1:string - button description
@app.post("/api/button") 
async def button(payload: dict= Body(...)):
    state = json.load(open("bombState.json","r"))
    if state['batteries'] == "":
        return {"value": "Error: battery amount and labels must be specified"}

    labels = state['labels'].split(" ")
    parts = re.split("[^a-zA-Z01]+", payload['p1'])
    color = parts[0].casefold()
    text = parts[1].casefold()
    batteries = int(state['batteries'])
    

    holdText = "Hold <br> Blue -> Release with 4 in timer <br> Yellow -> Release with 5 in timer <br> Otherwise -> Release with 1 in timer"
    if color == "blue" and text == "abort": 
        return {"value": holdText}
    
    if batteries > 0 and text == "detonate":
        return {"value": "Tap and release"}
    
    if color == "white" and "CAR1" in labels:
        return {"value": holdText}
    
    if batteries > 2 and "FRK1" in labels:
        return {"value": "Tap and release"}
    
    if color == "yellow":
        return {"value": holdText}
    
    if color == "red" and text == "hold":
        return {"value": "Tap and release"}
        
    return {"value": holdText}


@app.post("/api/keypad") 
async def keypad(payload: dict= Body(...)):
    return {"value": "Error: not implemented yet"}

#p1:string - the sequence of flashing buttons
@app.post("/api/simonsays") 
async def simon(payload: dict= Body(...)):
    state = json.load(open("bombState.json","r"))
    if state['strikes'] == "":
        return {"Value": "Error, number of strikes must be specified"}
    
    colorMap = {
        "r":"byg",
        "b":"rgr",
        "g":"yby",
        "y":"grb"
    }


    strikes = int(state['strikes'])
    ans = ""
    for char in payload["p1"]:
        char = char.lower()
        if char not in "rbgyu":
            continue
        
        ans += colorMap[char][strikes]
    return {"value": ans}

#p1:string - value on display
#p2:string - other values, in reading order
@app.post("/api/whosonfirst") 
async def whosonfirst(payload: dict= Body(...)):
    whosonDispMap = {
        "YES": 3,
        "FIRST": 2,
        "DISPLAY": 6,
        "OKAY": 2,
        "SAYS": 6,
        "NOTHING": 3,
        " ": 5,
        "BLANK": 4,
        "NO": 6,
        "LED": 3,
        "LEAD": 6,
        "READ": 4,
        "RED": 4,
        "REED": 5,
        "LEED": 5,
        "HOLD ON": 6,
        "YOU": 4,
        "YOU ARE": 6,
        "YOUR": 4,
        "YOU'RE": 4,
        "UR": 1,
        "THERE": 6,
        "THEY'RE": 5,
        "THEIR": 4,
        "THEY ARE": 3,
        "SEE": 6,
        "C": 2,
        "CEE": 6
    }

    whosonWordMap = {
        "READY": ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY", "NO", "FIRST", "UHHH", "NOTHING", "WAIT"],
        "FIRST": ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT", "READY", "BLANK", "WHAT", "PRESS", "FIRST"],
        "NO": ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING", "LEFT", "PRESS", "OKAY", "NO", "MIDDLE"],
        "BLANK": ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK", "PRESS", "READY", "NOTHING", "NO", "WHAT", "LEFT", "UHHH", "YES", "FIRST"],
        "NOTHING": ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT", "WHAT", "WAIT", "FIRST", "NOTHING", "READY"],
        "YES": ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING", "YES", "LEFT", "BLANK", "NO", "WAIT"],
        "WHAT": ["UHHH", "WHAT", "LEFT", "NOTHING", "READY", "BLANK", "MIDDLE", "NO", "OKAY", "FIRST", "WAIT", "YES", "PRESS", "RIGHT"],
        "UHHH": ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS", "BLANK", "UHHH", "MIDDLE", "WAIT", "FIRST"],
        "LEFT": ["RIGHT", "LEFT", "FIRST", "NO", "MIDDLE", "YES", "BLANK", "WHAT", "UHHH", "WAIT", "PRESS", "READY", "OKAY", "NOTHING"],
        "RIGHT": ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT", "MIDDLE", "LEFT", "UHHH", "BLANK", "OKAY", "FIRST"],
        "MIDDLE": ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT", "MIDDLE", "RIGHT", "FIRST", "UHHH", "YES"],
        "OKAY": ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY", "LEFT", "READY", "BLANK", "PRESS", "WHAT", "RIGHT"],
        "WAIT": ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT", "NOTHING", "READY", "RIGHT", "MIDDLE"],
        "PRESS": ["RIGHT", "MIDDLE", "YES", "READY", "PRESS", "OKAY", "NOTHING", "UHHH", "BLANK", "LEFT", "FIRST", "WHAT", "NO", "WAIT"],
        "YOU": ["SURE", "YOU ARE", "YOUR", "YOU'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?", "YOU", "UH UH", "LIKE", "DONE", "U"],
        "YOU ARE": ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU", "U", "YOU'RE", "SURE", "UR", "YOU ARE"],
        "YOUR": ["UH UH", "YOU ARE", "UH HUH", "YOUR", "NEXT", "UR", "SURE", "U", "YOU'RE", "YOU", "WHAT?", "HOLD", "LIKE", "DONE"],
        "YOU'RE": ["YOU", "YOU'RE", "UR", "NEXT", "UH UH", "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH", "SURE", "DONE", "LIKE", "HOLD"],
        "UR": ["DONE", "U", "UR", "UH HUH", "WHAT?", "SURE", "YOUR", "HOLD", "YOU'RE", "LIKE", "NEXT", "UH UH", "YOU ARE", "YOU"],
        "U": ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU'RE", "UR", "UH UH", "DONE", "U", "YOU", "LIKE", "HOLD", "YOU ARE", "YOUR"],
        "UH HUH": ["UH HUH", "YOUR", "YOU ARE", "YOU", "DONE", "HOLD", "UH UH", "NEXT", "SURE", "LIKE", "YOU'RE", "UR", "U", "WHAT?"],
        "UH UH": ["UR", "U", "YOU ARE", "YOU'RE", "NEXT", "UH UH", "DONE", "YOU", "UH HUH", "LIKE", "YOUR", "SURE", "HOLD", "WHAT?"],
        "WHAT?": ["YOU", "HOLD", "YOU'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE", "UH HUH", "UR", "NEXT", "WHAT?", "SURE"],
        "DONE": ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U", "YOU ARE", "UH UH", "DONE"],
        "NEXT": ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT", "LIKE", "DONE", "YOU ARE", "UR", "YOU'RE", "U", "YOU"],
        "HOLD": ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", "HOLD", "UH HUH", "YOUR", "LIKE"],
        "SURE": ["YOU ARE", "DONE", "LIKE", "YOU'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE", "U", "WHAT?", "NEXT", "YOUR", "UH UH"],
        "LIKE": ["YOU'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU", "LIKE", "SURE", "YOU ARE", "YOUR"]
    }

    dispPos = whosonDispMap[payload["p1"]]
    words = payload["p2"].split("-")
    wordList = whosonWordMap[words[dispPos-1]]
    for word in wordList:
        if word in words:
            return {"value": "press " + word}
    return {"value": "Error matching words: Make sure input is correct"}

#p1:string - displayed number, followed by button numbers left to right
#p2:string - previous buttons pressed, using format {position}{number}
@app.post("/api/memory") 
async def memory(payload: dict= Body(...)):
    nums = payload["p1"][1:]
    disp = int(payload["p1"][0])

    buttons = [int("1234"[i]+nums[i]) for i in range(0,4)]
    past = payload["p2"].strip().split(" ")
    stage = len(past)+1

    print(disp)
    print(buttons)
    print(past)

    ans = 99
    if past == [""] or past == ["0"]:
        stage = 1
    print(stage)
    if stage == 1:
        if disp == 1:
            ans = buttons[1]
        if disp == 2:
            ans = buttons[1]
        if disp == 3:
            ans = buttons[2]
        if disp == 4:
            ans = buttons[3]
    
    if stage == 2:
        if disp == 1:
            ans = buttons[nums.index("4")] #press the 4
        if disp == 2:
            ans = buttons[int(past[0][0])-1] #same position as stage 1
        if disp == 3:
            ans = buttons[0] #pos 1
        if disp == 4:
            ans = buttons[int(past[0][0])-1]
    
    if stage == 3:
        if disp == 1:
            ans = buttons[nums.index(past[1][1])] # same label as stage 2
        if disp == 2:
            ans = buttons[nums.index(past[0][1])] # same label as stage 1
        if disp == 3:
            ans = buttons[2]
        if disp == 4:
            ans = buttons[nums.index("4")]
    
    if stage == 4:
        if disp == 1:
            ans = buttons[int(past[0][0])-1]
        if disp == 2:
            ans = buttons[0]
        if disp == 3:
            ans = buttons[int(past[1][0])-1]
        if disp == 4:
            ans = buttons[int(past[1][0])-1]

    if stage == 5:
        if disp == 1:
            ans = buttons[nums.index(past[0][1])]
        if disp == 2:
            ans = buttons[nums.index(past[1][1])]
        if disp == 3:
            ans = buttons[nums.index(past[3][1])]
        if disp == 4:
            ans = buttons[nums.index(past[2][1])]
    return {"value": ans}
#p1:string - the morse code, given by - and . Spaces are maybe included 
@app.post("/api/morse") 
async def morse(payload: dict= Body(...)):
    morseMap = {
        "-.....--...": "beats",
        "-........-.-.---": "bistro",
        "-...------......": "bombs",
        "-...----..-....": "boxes",
        "-....-...--.-": "break",
        "-....-...-.-.-.-": "brick",
        "-.-...-.-.-.-": "trick",
        "..-..-....-.-.-.-": "flick",
        ".....-.-...-.....": "halls",
        ".-....--.-...": "leaks",
        ".........-...-..": "shell",
        "....-....-.-.-.-": "slick",
        "...-..--.-": "steak",
        "...-..-.--.": "sting",
        "...-.-.----....": "strobe",
        "...-.-.-.----.-.": "vector"
    }

    morseFreqMap = {
        "shell": 3.505 ,
        "halls": 3.515 ,
        "slick": 3.522 ,
        "trick": 3.532 ,
        "boxes": 3.535 ,
        "leaks": 3.542 ,
        "strobe": 3.545 ,
        "bistro": 3.552 ,
        "flick": 3.555 ,
        "bombs": 3.565 ,
        "break": 3.572 ,
        "brick": 3.575 ,
        "steak": 3.582 ,
        "sting": 3.592 ,
        "vector": 3.595 ,
        "beats": 3.600
    }

    code = "".join(payload["p1"].split(" "))
    options = []
    try: 
        word = morseMap[code]
        options = [str(morseFreqMap[word])]

    except KeyError:
        for key in morseMap.keys():
            if key.startswith(code):
                options.append(str(morseFreqMap[morseMap[key]]))
                break
    if options == []:
        options = ["No match found, make sure input is correct and starts from beginning"]
    return {"value": " or ".join(options)}

#p1:string(int?) - lights, left to right
#p2:string - wire colors, separated by spaces
#p3:string(int?) - star state, left to right
@app.post("/api/compwires") 
async def compwires(payload: dict= Body(...)):
    state = json.load(open("bombState.json","r"))
    if state['serial'] == "" or state["batteries"] == 0:
        return {"value": "Error: Serial, batteries and ports must be given"}
    
    digit = int(state['serial'][0]) % 2 == 0
    parallel = "parallel" in state["ports"]
    batteries = int(state['batteries']) >= 2
    colors = re.split('[^rbwv]', payload["p2"])

    print(payload["p1"])
    print(colors)
    print(payload["p3"])
    instructionMap = {
        "C": "Cut",
        "D": "Dont",
        "S": "Cut" if digit else "Dont",
        "P": "Cut" if parallel else "Dont",
        "B": "Cut" if batteries else "Dont"
    }

    compwireMap = {
        0b0000: "C",
        0b0001: "C",
        0b0010: "S",
        0b0011: "C",
        0b0100: "S",
        0b0101: "D",
        0b0110: "S",
        0b0111: "P",
        0b1000: "D",
        0b1001: "B",
        0b1010: "B",
        0b1011: "B",
        0b1100: "P",
        0b1101: "P",
        0b1110: "S",
        0b1111: "D"
    }

    answer = []


    for i in range(len(payload["p1"])):
        group = ((payload["p3"][i] == "1")    #star
                + 2*("r" in colors[i])      #red
                + 4*("b" in colors[i])      #blue
                +8*(payload["p1"][i] == "1")) #light
        print(group)
        answer.append(instructionMap[compwireMap[group]])
    return {"value": "-".join(answer)}
        




#p1:string - wires from top to bottom, in format {color}{dest}, separated with space (BC, BA, UC)
#p2:string - past wire counts, ordered {#red}{#blue}{#black}
@app.post("/api/wiresequence") 
async def wiresequence(payload: dict= Body(...)):
    red = ["C", "B", "A", "AC", "B", "AC", "ABC", "AB", "B"]
    blue = ["B", "AC", "B", "A", "B", "BC", "C", "AC", "A"]
    black = ["ABC", "AC", "B", "AC", "B", "BC", "AB", "C", "C"]
    counts = re.split("[^0-9]+", payload["p2"])
    if len(counts) < 4:
        counts = ["", "0", "0", "0"]
    redCount = min(int(counts[1]),8)
    blueCount = min(int(counts[2]),8)
    blackCount = max(int(counts[3]),8)
    wires = payload["p1"].upper().split(" ")

    print(wires)
    targets = []
    for i in range(len(wires)):
        wire=wires[i]
        if wire[0] == "R":
            if wire[1] in red[redCount]:
                targets.append(str(i+1))
            redCount += 1
        if wire[0] == "U":
            if wire[1] in blue[blueCount]:
                targets.append(str(i+1))
            blueCount += 1
        if wire[0] == "B":
            if wire[1] in black[blackCount]:
                targets.append(i+1)
            blackCount += 1
    if targets == []:
        targets = ["nothing"]
    return {"value": "Cut " + " and ".join(targets) }
        
            
            





#p1:string - identifier position
#p2:string - starting position
#p3:string - goal position
@app.post("/api/maze") 
async def maze(payload: dict= Body(...)):
    maze1 = [""]
    
    return {"value": "Error: not implemented yet"}



#p1:string - options for first char(or empty)
#p2:string - options for second char(or empty)
#p3:string - options for third char(or empty)
#p4:string - options for fourth char(or empty)
#p5:string - options for fifth char(or empty)
@app.post("/api/passwords")
async def passwords(payload: dict= Body(...)):  
    chars = ["p1", "p2", "p3", "p4", "p5"]
    solutions = ["about", "after", "again", "below", "could", 
                 "every", "first", "found", "great", "house",
                 "large", "learn", "never", "other", "place",
                   "plant", "point", "right", "small", "sound",
                 "spell", "still", "study", "their", "there",
                 "these", "thing", "think", "three", "water",
                 "where", "which", "world", "would", "write"]
    for char in chars:
        if char in payload.keys():
            options = payload[char]
            if len(options) != 6:
                continue
            index = chars.index(char)
            solutions = [s for s in solutions if s[index] in options]
    possibilities = " or ".join(solutions)
    return {"value": possibilities}

#p1 - light state of top row, only 3 given => rightmost 3
#p2 - light state of bot row, only 3 given => rightmost 3
@app.post("/api/knobs") 
async def knobs(payload: dict= Body(...)):
    return {"value": "Error: not implemented yet"}





@app.post("/api/updateBomb")
async def updateBomb(payload: dict= Body(...)):
    with open("bombState.json", "w") as file:
    
        json.dump(payload,file)
    return {"value": "Bomb status updated"}

if __name__ == "__main__":
    uvicorn.run(app, port=8001)