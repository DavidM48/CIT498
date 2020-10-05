var modalLoadData = document.getElementById("modalLoadData");
var modalControls = document.getElementById("modalControls");

var btnLoadData = document.getElementById("btnLoadData");
var btnControls = document.getElementById("btnControls");
var btnRotate = document.getElementById("btnRotate");
var btnReset = document.getElementById("btnReset");

var btnControlsConfirm = document.getElementById("btnControlsConfirm");
var btnDataConfirm = document.getElementById("btnDataConfirm");

var btnShuffle = document.getElementById("btnShuffle");
var btnMoves = document.getElementById("btnMoves");

btnLoadData.onclick = function() {
    modalLoadData.style.display = "block";
}

btnControls.onclick = function() {
    modalControls.style.display = "block";
}

btnControlsConfirm.onclick = function() {
    modalControls.style.display = "none";
}

btnDataConfirm.onclick = function() {
    modalLoadData.style.display = "none";
    btnShuffle.style.visibility = "visible";
}

window.onclick = function(event) {
  if (event.target == modalLoadData) {
    modalLoadData.style.display = "none";
  }else if (event.target == modalControls){
    modalControls.style.display = "none";
  }
} 

btnReset.onclick = function() {
    btnMoves.style.visibility = "hidden";
    btnShuffle.style.visibility = "hidden";
    removeCubes();
    refresh(false,3);
}

var rotateI, rotatePlain, rotateReverse;

btnRotate.onclick = function() {
    rotateI = document.querySelector(".rotateI").value;
    rotatePlain = document.querySelector(".rotatePlain").value;
    rotateReverse = document.querySelector(".rotateReverse").checked;

    if(rotateI > 2)
        rotateI = 2;
    else if (rotateI < 0)
        rotateI = 0;

    if(rotatePlain > 2)
        rotatePlain = 2;
    else if (rotatePlain < 0)
        rotatePlain = 0;
        
    rotate(rotateI,rotatePlain,rotateReverse);
}

btnShuffle.onclick = function() {
    file = document.querySelector(".selectFile").value;
    if (file != undefined)
        stepThroughMovesStart(true, file);
    btnMoves.style.visibility = "visible";
}

btnMoves.onclick = function() {
    stepThroughMovesStartWithExistingFile(); 
}
