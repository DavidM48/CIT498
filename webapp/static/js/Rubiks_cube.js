class helper {
    constructor() {
        //alert("Helper was constructed");
    }

    side(color) {
        return this.SideDict(color);
    }

    SideDict(side) {
        if (typeof side == "number")
            return side
        if (side === "south")
            var x = 0;
        else if (side === "north")
            var x = 1;
        else if (side === "top")
            var x = 2;
        else if (side === "bottom")
            var x = 3;
        else if (side === "west")
            var x = 4;
        else if (side === "east")
            var x = 5;
        else if (side === 0)
            var x = "south";
        else if (side === 1)
            var x = "north";
        else if (side === 2)
            var x = "top";
        else if (side === 3)
            var x = "bottom";
        else if (side === 4)
            var x = "west";
        else if (side === 5)
            var x = "east";
        else
            var x = -1;
        return x;
    }

    color(color) {
        return this.ColorDict(color);
    }

    ColorDict(color) {
        if (typeof color == "number")
            return color
        if (color === "White")
            var x = 1;
        else if (color === "Red")
            var x = 2;
        else if (color === "Green")
            var x = 3;
        else if (color === "Blue")
            var x = 4;
        else if (color === "Orange")
            var x = 5;
        else if (color === "Yellow")
            var x = 6;
        else if (color === 1)
            var x = "White";
        else if (color === 2)
            var x = "Red";
        else if (color === 3)
            var x = "Green";
        else if (color === 4)
            var x = "Blue";
        else if (color === 5)
            var x = "Orange";
        else if (color === 6)
            var x = "Yellow";
        else
            var x = 6;
        return x;
    }

    colorHex(color) {
        return this.hexDict(color)
    }

    hexDict(color) {
        var x = 0xbfdef5; //Same as background
        //var x = 0xa7f542;
        //var x = 0x000000; //Black
        if (color === 1)
            x = 0xffffff;
        else if (color === 2)
            x = 0xff0000;
        else if (color === 3)
            x = 0x00ff00; 
        else if (color === 4)
            x = 0x0000ff;
        else if (color === 5)
            x = 0xffae00;
        else if (color === 6)
            x = 0xffff00;
        return x;
    }
}

class square {
    h = new helper();

    color; 
    postion;

    constructor(color) {
        this.setColor(color);
        this.setPos(color);
    }

    setColor(color) {
        this.color = this.h.hexDict(color);
    }

    setPos(pos){
        this.postion = pos;
    }

    setColorOverride(color){
        this.color = color
    }

    getColor(){
        return this.color
    }

    getPos(){
        return this.postion
    }

    getColorString() {
        return this.h.colorHex(this.color).toString(16);
    }
}

class cube {
    h = new helper();
    
    cube;
    queueReady;
    sides;

    constructor() {
        this.cube = [new square(1),
            new square(2),
            new square(3),
            new square(4),
            new square(5),
            new square(6)];
        this.queueReady = false;
        this.sides = 6;  
    }

    setCords(x, y, z){
        this.x = x;
        this.y = y;
        this.z = z;
    }   

    getCords(){
        return [this.x, this.y, this.z];
    }

    getColorArray(){
        var array = [this.cube[0].getColor(),
        this.cube[1].getColor(),
        this.cube[2].getColor(),
        this.cube[3].getColor(),
        this.cube[4].getColor(),
        this.cube[5].getColor()];
        return array;
    }

    getPositionArray(){
        var array = [this.cube[0].getPos(),
                this.cube[1].getPos(),
                this.cube[2].getPos(),
                this.cube[3].getPos(),
                this.cube[4].getPos(),
                this.cube[5].getPos()];
        return array;
    }

    swapQueue(cube){
        if (this.queueReady)
            console.log("Warning: This cube already has a pair {}".format(this.getCords()));
            
        if (this.sides == cube.getNumberOfSides()){
            this.queue = cube.getPositionArray();
            this.queueReady = true;
        }else
            console.log("Either object was not a cube or sides missmatch");
    }

    swapCommitQueue(){
        if (!this.queueReady){
            //print("Warning: This cube is not ready to swap {}".format(this.getCords()))
            return;
        }

        this.setSide(0, this.queue[0]);
        this.setSide(1, this.queue[1]);
        this.setSide(2, this.queue[2]);
        this.setSide(3, this.queue[3]);
        this.setSide(4, this.queue[4]);
        this.setSide(5, this.queue[5]);
        this.queue = [];
        this.queueReady = false;
    }

    queueState(){
        return this.queueReady;
    }

    rotateCube(plain, reverse){
        var temp = this.getPositionArray();
        if (plain == 0){
            if (reverse){
                this.cube[0] = new square(temp[2])
                this.cube[1] = new square(temp[3])
                this.cube[2] = new square(temp[1])
                this.cube[3] = new square(temp[0])
            }else{
                this.cube[0] = new square(temp[3])
                this.cube[1] = new square(temp[2])
                this.cube[2] = new square(temp[0])
                this.cube[3] = new square(temp[1])
            }
        }else if (plain == 1){
            if (reverse){
                this.cube[2] = new square(temp[4])
                this.cube[3] = new square(temp[5])
                this.cube[4] = new square(temp[3])
                this.cube[5] = new square(temp[2])
             }else{
                this.cube[2] = new square(temp[5])
                this.cube[3] = new square(temp[4])
                this.cube[4] = new square(temp[2])
                this.cube[5] = new square(temp[3])
             }
        }else{
            if (reverse){
                this.cube[0] = new square(temp[4])
                this.cube[1] = new square(temp[5])
                this.cube[4] = new square(temp[1])
                this.cube[5] = new square(temp[0])
            }else{
                this.cube[0] = new square(temp[5])
                this.cube[1] = new square(temp[4])
                this.cube[4] = new square(temp[0])
                this.cube[5] = new square(temp[1])
            }
        }
    }

    setSide(side, color){
        this.cube[side] = new square(color)
    }

    setSideOverride(side, color){
        this.cube[side].setColorOverride(color)
    }

    removeSide(side){
        this.cube[side].setColor(0)
        this.cube[side].setPos(0)
        this.sides -= 1
    }

    getNumberOfSides(){
        return this.sides
    }

    getCube(){
        return this.cube
    }

    getSquare(side){
        return this.cube[side]
    }

    setSquare(side, sq){
        this.cube[side].setColorHex(sq.getColor())
    }
}

class rubiks_cube {
    h = new helper();

    rubiks;
    size;

    constructor(size) {
        this.size = size;
        this.initArray();
        this.fillRubiks();
    }

    initArray() {
        this.rubiks = new Array(this.size);
        for (var x = 0; x < this.size; x++) {
            this.rubiks[x] = new Array(this.size);
            for (var y = 0; y < this.size; y++) 
                this.rubiks[x][y] = new Array(this.size);;
        }
    }

    fillRubiks() {
        var top = this.size - 2
        for (var x = 0; x < this.size; x++)
            for (var y = 0; y < this.size; y++)
                for (var z = 0; z < this.size; z++) {
                    this.rubiks[x][y][z] = new cube();
                    this.rubiks[x][y][z].setCords(x,y,z);
                    if (x <= top)
                        this.rubiks[x][y][z].removeSide(0); 
                    if (x >= 1)
                        this.rubiks[x][y][z].removeSide(1);

                    if (y <= top)
                        this.rubiks[x][y][z].removeSide(2);
                    if (y >= 1)
                        this.rubiks[x][y][z].removeSide(3);

                    if (z <= top)
                        this.rubiks[x][y][z].removeSide(4);
                    if (z >= 1)
                        this.rubiks[x][y][z].removeSide(5);
                }
    }

    fetchRubiks() {
        return this.rubiks;
    }
    getSize(){
        return this.size;
    }

    rotateRubiks(i, plain, reverse){
        //this.logMoves[this.logCount] = {"i":i,"plain":plain,"reverse":reverse}
        //this.logCount = this.logCount + 1

        //if (i >= this.size or i < 0)
            //raise ValueError("i is either to big or too small.")

        var sliced = [];
        //Fill the list with the cubes we need to swap
        for (var x = 0; x < this.size; x++)
            for(var y = 0; y < this.size; y++){
                if (plain == 0)
                    sliced.push((this.rubiks[x][y][i]))
                else if (plain == 1)
                    sliced.push((this.rubiks[i][x][y]))
                else
                    sliced.push((this.rubiks[x][i][y]))
            }
        //Only works with 3x3x3
        if (reverse){
            sliced[0].swapQueue(sliced[6])
            sliced[1].swapQueue(sliced[3])
            sliced[2].swapQueue(sliced[0])
            sliced[3].swapQueue(sliced[7])
            sliced[5].swapQueue(sliced[1])
            sliced[6].swapQueue(sliced[8])
            sliced[7].swapQueue(sliced[5])
            sliced[8].swapQueue(sliced[2])
        }else{
            sliced[0].swapQueue(sliced[2])
            sliced[1].swapQueue(sliced[5])
            sliced[2].swapQueue(sliced[8])
            sliced[3].swapQueue(sliced[1])
            sliced[5].swapQueue(sliced[7])
            sliced[6].swapQueue(sliced[0])
            sliced[7].swapQueue(sliced[3])
            sliced[8].swapQueue(sliced[6])
        }

        for (var x = 0; x < sliced.length; x++){
            sliced[x].swapCommitQueue()
            sliced[x].rotateCube(plain, reverse)
        }
    }
}