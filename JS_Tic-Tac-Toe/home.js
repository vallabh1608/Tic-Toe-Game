let boxes=document.querySelectorAll(".box");
let resetbtn=document.querySelector("#reset");
let msg=document.querySelector(".msg-container");
let reset=document.querySelector("#reset");
let newgame=document.querySelector(".newgame");

newgame.classList.add("hide");
let turn0=true;
const WinPatterns=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6] 
];

boxes.forEach((box)=>{
   box.addEventListener("click",()=>{
    if (turn0==true){
        box.innerText="O";
        turn0=false;
    }
    else{
        box.innerText="X";
        turn0=true;
    }
    box.disabled=true;  
    checkwinner();
    
   });
});
const resetgame=()=>{
    turn0=true;
    enableAllboxes();
    clear();
    newgame.classList.add("hide");
    msg.innerText="";
    resetbtn.classList.remove("hide");

};
const checkwinner=()=>{
    for (let pattern of WinPatterns){
        if (boxes[pattern[0]].innerText==="X" && boxes[pattern[1]].innerText==="X" && boxes[pattern[2]].innerText==="X"){
            msg.innerText="Winner is X";
            removehide();
            disableAllboxes();
            resetbtn.classList.add("hide");
        }
        else if(boxes[pattern[0]].innerText==="O" && boxes[pattern[1]].innerText==="O" && boxes[pattern[2]].innerText==="O"){
            msg.innerText="Winner is O";
            removehide();
            disableAllboxes();
            resetbtn.classList.add("hide");
        }
    };
};
const disableAllboxes=()=>{
    boxes.forEach((box)=>{
        box.disabled=true;

    })
};
const enableAllboxes=()=>{
    boxes.forEach((box)=>{
    box.disabled=false;
    })
};
const clear=()=>{
    boxes.forEach((box)=>{
        box.innerText='';
    })
};
const removehide=()=>{
    newgame.classList.remove("hide");
}

reset.addEventListener("click",resetgame);

newgame.addEventListener("click",resetgame);