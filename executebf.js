

var executebf = function(bf){
    var out = "";
    var hexs = "0123456789ABCDEF";
    
    var stack = [0];//default 0
    var pc = 0;
    var ptr = 0;
    while(true){
        var ins = bf[pc];
        switch(ins){
            case ">":
            ptr++;
            if(ptr === stack.length){
                //add one cell
                stack.push(0);
            }
            break;
            case "<":
            ptr--;
            if(ptr < 0){
                console.log("error, buffer overflow, check y' code. pointer smaller than 0");
                return false;
            }
            break;
            case "+":
            stack[ptr] = (stack[ptr]+1)&15;
            break;
            case "-":
            stack[ptr] = (stack[ptr]+15)&15;
            break;
            case ".":
            out += hexs[stack[ptr]];
            break;
            case ",":
            
            break;
            case "[":
            if(stack[ptr] === 0){
                var openparens = 0;
                while(true){
                    pc++;
                    if(openparens === 0 && bf[pc] === "]")break;
                    if(pc >= bf.length){
                        console.log("buffer overflow, program counter larger than the program");
                        return false;
                    }
                    if(bf[pc] === "["){
                        openparens++;
                    }else if(bf[pc] === "]"){
                        openparens--;
                    }
                }
            }
            break;
            case "]":
            if(stack[ptr] !== 0){
                var openparens = 0;
                while(true){
                    pc--;
                    if(openparens === 0 && bf[pc] === "[")break;
                    if(pc < 0){
                        console.log("buffer overflow, program counter lower than 0");
                        return false;
                    }
                    if(bf[pc] === "]"){
                        openparens++;
                    }else if(bf[pc] === "["){
                        openparens--;
                    }
                }
            }
            break;
        }
        pc++;
        if(pc >= bf.length){
            console.log("execution success, returning");
            break;
        }
    }
    return out;
};

module.exports = executebf;
