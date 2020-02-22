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
        if (side === "West")
            var x = 0;
        else if (side === "South")
            var x = 1;
        else if (side === "North")
            var x = 2;
        else if (side === "East")
            var x = 3;
        else if (side === "Top")
            var x = 4;
        else if (side === "Bottom")
            var x = 5;
        else if (side === 0)
            var x = "West";
        else if (side === 1)
            var x = "South";
        else if (side === 2)
            var x = "North";
        else if (side === 3)
            var x = "East";
        else if (side === 4)
            var x = "Top";
        else if (side === 5)
            var x = "Bottom";
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
            var x = 0;
        else if (color === "Red")
            var x = 1;
        else if (color === "Green")
            var x = 2;
        else if (color === "Blue")
            var x = 3;
        else if (color === "Orange")
            var x = 4;
        else if (color === "Yellow")
            var x = 5;
        else if (color === 0)
            var x = "White";
        else if (color === 1)
            var x = "Red";
        else if (color === 2)
            var x = "Green";
        else if (color === 3)
            var x = "Blue";
        else if (color === 4)
            var x = "Orange";
        else if (color === 5)
            var x = "Yellow";
        else
            var x = 6;
        return x;
    }

    colorHex(color) {
        return this.hexDict(color)
    }

    hexDict(color) {
        if (color === 0)
            var x = 0xffffff;
        else if (color === 1)
            var x = 0xff0000;
        else if (color === 2)
            var x = 0x00ff00;
        else if (color === 3)
            var x = 0x0000ff;
        else if (color === 4)
            var x = 0xffae00;
        else if (color === 5)
            var x = 0xffff00;
        else
            var x = 0x000000;
        return x;
    }
}

class square {
    h = new helper();
    side;
    color;
    constructor(side, color) {
        this.side = side;
        this.color = color;
    }

    setSide(side) {
        this.side = side;
    }

    setColor(color) {
        this.color = color;
    }

    getSide() {
        return this.side;
    }

    getColorString() {
        return this.h.colorHex(this.color).toString(16);
    }

    getColor() {
        return this.h.colorHex(this.color);
    }
}

class cube {
    h = new helper();
    constructor(def) {
        if (def) {
            this.cube = [new square(0, 0),
                new square(1, 1),
                new square(2, 2),
                new square(3, 3),
                new square(4, 4),
                new square(5, 5)
            ];
        }
    }

    addSide(side, color) {
        this.cube[this.h.side(side)] = square(side, color);
    }

    removeSide(side) {
        this.cube[this.h.side(side)].setColor(this.h.color(6));
    }

    getCube() {
        return this.cube;
    }

    getSquare(side) {
        return this.cube[this.h.side(side)];
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
            for (var y = 0; y < this.size; y++) {
                this.rubiks[x][y] = new Array(this.size);;
            }
        }
    }

    defaultCube() {
        this.dc = cube(true)
    }

    fillRubiks() {
        for (var x = 0; x < this.size; x++)
            for (var y = 0; y < this.size; y++)
                for (var z = 0; z < this.size; z++) {
                    this.rubiks[x][y][z] = new cube(true);
                    if (y <= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(1));
                    if (y >= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(2));
                    if (z <= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(3));
                    if (z >= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(0));
                    if (x <= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(5));
                    if (x >= 1)
                        this.rubiks[x][y][z].removeSide(this.h.side(4));
                }
    }

    fetchRubiks() {
        return this.rubiks;
    }
}