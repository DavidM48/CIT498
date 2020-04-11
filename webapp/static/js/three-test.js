var camera, controls, scene, renderer, geometry, size, rb, array, renderedCubes, boxSize;

scene = new THREE.Scene();
scene.background = new THREE.Color( 0xcccccc );
scene.fog = new THREE.FogExp2( 0xff0000, 0.002 );

renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

camera = new THREE.PerspectiveCamera( 60, window.innerWidth / window.innerHeight, 1, 1000 );
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

boxSize = 0.85
geometry = new THREE.BoxGeometry(boxSize, boxSize, boxSize);

var jsonObj
var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200)
    jsonObj = JSON.parse(this.responseText);
};

xmlhttp.open("GET", "./static/test.json", true);
xmlhttp.send(); 
alert("wow")

size = jsonObj.size

function onWindowResize(){
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}

var createCubes = function() {
    rb = new rubiks_cube(size);
    //array = rb.fetchRubiks();
    renderedCubes = rb.initArray();

    for (var x = 0; x < size; x++)
            for (var y = 0; y < size; y++)
                for (var z = 0; z < size; z++) {
                    var material = [new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[0]}),
                    new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[1]}),
                    new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[2]}),
                    new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[3]}),
                    new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[4]}),
                    new THREE.MeshBasicMaterial({color:jsonObj[x][y][z].colors[5]})]; 
                    
                    renderedCubes[x][y][z] = new THREE.Mesh(geometry, material);
                    renderedCubes[x][y][z].position.set(x,y,z);
                    scene.add(renderedCubes[x][y][z]);
                }
    return(renderedCubes)
}

var updateCubeColor = function(x,y,z,color){
    renderedCubes[x][y][z] = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({color:color}));
    renderedCubes[x][y][z].position.set(x,y,z);
    scene.add(renderedCubes[x][y][z]);
}

var animate = function() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
};

window.addEventListener( 'resize', onWindowResize, false );

createCubes()
animate()