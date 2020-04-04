import * as THREE from '../librarys/build/three.module.js';
import { OrbitControls } from '../librarys/OrbitControls.js';

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

controls = new OrbitControls( camera, renderer.domElement );
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.screenSpacePanning = false;
controls.minDistance = 1;
controls.maxDistance = 100;
controls.maxPolarAngle = Math.PI;

boxSize = 0.998
geometry = new THREE.BoxGeometry(boxSize, boxSize, boxSize);

size = 3

var createCubes = function() {
    rb = new rubiks_cube(size);
    array = rb.fetchRubiks();
    renderedCubes = rb.initArray();

    for (var x = 0; x < size; x++)
            for (var y = 0; y < size; y++)
                for (var z = 0; z < size; z++) {
                    var material = [new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(0).getColor()}),
                    new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(1).getColor()}),
                    new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(2).getColor()}),
                    new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(3).getColor()}),
                    new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(4).getColor()}),
                    new THREE.MeshBasicMaterial({color:array[x][y][z].getSquare(5).getColor()})]; 
                    
                    renderedCubes[x][y][z] = new THREE.Mesh(geometry, material);
                    renderedCubes[x][y][z].position.set(x,y,z);
                    scene.add(renderedCubes[x][y][z]);
                }
    return(renderedCubes)
}

var animate = function() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
};

createCubes()
animate()