const boardLength = 9;
function checker(board,row,col,val) {
    //Row and Column checker.
    for(var i=0;i<boardLength;i++) {
        if(board[row][i] == val) return false;
        if(board[i][col] == val) return false;
    }
    //Sub-matrix checker.
    let startRow = row - row%3;
    let startCol = col - col%3;
    for(var i=0;i<3;i++) {
        for(var j=0;j<3;j++) {
            if(board[startRow+i][startCol+j] == val)
                return false;
        }
    } 
    return true;
}
function solveBoard(board,row,col) {
    if(row == boardLength-1 && col == boardLength)
        return true;
    
    if(col == boardLength) {
        row = row + 1;
        col = 0;
    }

    if(board[row][col] > 0) {
        return solveBoard(board,row,col+1);
    }

    for(var val=1;val<=boardLength;val++) {
        if(checker(board,row,col,val)) {
            board[row][col] = val;
            if(solveBoard(board,row,col+1)) {
                return true;
            }
        }
        board[row][col] = 0;
    }

    return false;
    
}
function fillBoard() {
    var board = new Array();
    for(var i=0;i<boardLength;i++) {
        var row = new Array();
        for(var j=0;j<boardLength;j++) {
            let id = i.toString() + j.toString();
            row.push(parseInt(document.getElementById(id).value));
        }
        board.push(row);
    }
    if(solveBoard(board,0,0)) {
        for(var i=0;i<boardLength;i++) {
            for(var j=0;j<boardLength;j++) {
                let id = i.toString() + j.toString();
                //console.log(board[i][j]);
                document.getElementById(id).value = board[i][j].toString();
            }
        }
    } else {
        document.write("Unsolvable.....")
    }
    
}
var resetBoard = function() {
    window.location.reload();
}