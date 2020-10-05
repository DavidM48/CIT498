var camera, controls, scene, renderer, renderPass, geometry, composer, clock, rb, array, renderedCubes, boxSize, rubiks, cubeExists, interval, moves, stepCounter, id;

scene = new THREE.Scene();
scene.background = new THREE.Color( 0xbfdef5 );
scene.fog = new THREE.FogExp2( 0xff0000, 0.002 );

renderer = new THREE.WebGLRenderer( { canvas: myCanvasID, antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, (window.innerHeight - 47) );
document.body.appendChild( renderer.domElement );

clock = new THREE.Clock();

camera = new THREE.PerspectiveCamera( 60, window.innerWidth / (window.innerHeight - 47), 1, 1000 );
camera.position.set( 10, 10, 10 );


controls = import('../librarys/OrbitControls.js')
    .then((module) => {
        return new module.OrbitControls( camera, renderer.domElement );
    });

controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.screenSpacePanning = false;
controls.minDistance = 1;
controls.maxDistance = 100;
controls.maxPolarAngle = Math.PI;

composer = new POSTPROCESSING.EffectComposer( renderer );
composer.addPass(new POSTPROCESSING.RenderPass(scene, camera));

boxSize = 0.9;
geometry = new THREE.BoxBufferGeometry(boxSize, boxSize, boxSize);

var jsonObj;
var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200){
        jsonObj = JSON.parse(this.responseText);
        console.log("Retrived File");
  }
}

function getJSONFile(file) {
    if (file == undefined)
        xmlhttp.open("GET", "../static/1588550410404.json", true);
    else{
        filelocation = "../static/".concat(file)
        xmlhttp.open("GET", filelocation, true);
    }
    xmlhttp.send(); 
}

function onWindowResize() {
    camera.aspect = window.innerWidth / (window.innerHeight - 47);
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, (window.innerHeight - 47) );
}

function creat3DArray(size){
    emptyArray = new Array(size);
    for (var x = 0; x < size; x++) {
        emptyArray[x] = new Array(size);
        for (var y = 0; y < size; y++)
            emptyArray[x][y] = new Array(size);
    }
    return(emptyArray)
}

function createCubes(fromJSON) {
    var size, offset;
    rubiksLocale = rubiks.fetchRubiks();
    if (fromJSON){
        size = jsonObj.size;
        renderedCubes = creat3DArray(size);
    }else{
        size = rubiks.getSize()
        renderedCubes = creat3DArray(size);
    }
    offset = Math.floor(size/2)

    for (var x = 0; x < size; x++)
            for (var y = 0; y < size; y++)
                for (var z = 0; z < size; z++) {
                    var material, colors;
                    if (fromJSON){
                        material = [new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[0]}),
                        new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[1]}),
                        new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[2]}),
                        new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[3]}),
                        new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[4]}),
                        new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[5]})]; 
                    }else{
                        colors = rubiksLocale[x][y][z].getColorArray();
                        material = [new THREE.MeshBasicMaterial({color:colors[0]}),
                        new THREE.MeshBasicMaterial({color:colors[1]}),
                        new THREE.MeshBasicMaterial({color:colors[2]}),
                        new THREE.MeshBasicMaterial({color:colors[3]}),
                        new THREE.MeshBasicMaterial({color:colors[4]}),
                        new THREE.MeshBasicMaterial({color:colors[5]})]; 
                    }

                    renderedCubes[x][y][z] = new THREE.Mesh(geometry, material);
                    renderedCubes[x][y][z].position.set(x - offset, y - offset, z - offset);

                    if(fromJSON){
                        if (jsonObj[x][y][z].sides > 0)
                            scene.add(renderedCubes[x][y][z]);
                    }else{
                        if (rubiksLocale[x][y][z].getNumberOfSides() > 0)
                            scene.add(renderedCubes[x][y][z]);
                    }
                }
                cubeExists = true;
}

function creatRubiksObject(size){
    this.size = size;
    this.rubiks = new rubiks_cube(size);
}

function updateCubeColor(x,y,z,color){
    renderedCubes[x][y][z] = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({color:color}));
    renderedCubes[x][y][z].position.set(x,y,z);
    scene.add(renderedCubes[x][y][z]);
}

//Most likly not the best way to remove cubes
function removeCubes(){
    if (!cubeExists)
        console.log("Cube might not exist")
    for (var x = 0; x < this.size; x++)
            for (var y = 0; y < this.size; y++)
                for (var z = 0; z < this.size; z++) {
                    scene.remove(renderedCubes[x][y][z]);
                    //renderer.removeObject( scene, renderedCubes[x][y][z] );
                    renderedCubes[x][y][z].geometry.dispose;
                    renderedCubes[x][y][z].material.dispose;
                    renderedCubes[x][y][z] = undefined;
                } 
    cubeExists = false; 

    animate();           
}

function animate() {
    if (id != undefined)
        cancelAnimationFrame( id );
    id = requestAnimationFrame(animate);
    composer.render(clock.getDelta());
}

function startRender(fromJSON) {
    createCubes(fromJSON);
    animate();
}

function refresh(fromJSON, size) {
    if (fromJSON){
        getJSONFile();
        alert("Refeshing from json");
    }else{
        console.log("Creating from object")
        if (size < 3) size = 3;
        creatRubiksObject(size);
    } 
    //removeCubes();
    startRender(fromJSON); 
}

function rotate(i, plain, reverse){
    rubiks.rotateRubiks(i, plain, reverse);
    removeCubes();
    startRender(false);
}

function stepThroughMovesStart(shuffleMove, file){
    if (file == undefined)
        getJSONFile()
    else
        getJSONFile(file)
    alert("Refeshing from json");
    if (shuffleMove)
        this.moves = jsonObj.movesShuffle;
    else
        this.moves = jsonObj.moves;
    this.stepCounter = 0;
    this.interval = window.setInterval(stepThroughMoves, 150);
}

function stepThroughMovesStartWithExistingFile(){
    this.moves = jsonObj.moves;
    this.stepCounter = 0;
    this.interval = window.setInterval(stepThroughMoves, 50);
}

function stepThroughMoves(){
    if (stepCounter < moves.steps){
        rotate(moves[stepCounter][0], moves[stepCounter][1], moves[stepCounter][2]);
        stepCounter++;
    }else{
        window.clearInterval(interval);
    }   
}

window.addEventListener('resize', onWindowResize, false);

cubeExists = false;
refresh(false,3);