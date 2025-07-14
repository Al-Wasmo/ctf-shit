
function swap_away(i, j) {
    const boardChildren = board.children;
    const el1 = boardChildren[i];
    
    // Check if j is out of bounds (storage operation)
    if (j >= boardChildren.length || j < 0) {
        if (!el1) return; // Can't move non-existent element
        
        // Create storage board if it doesn't exist
        let storageBoard = document.getElementById('board2');
        if (!storageBoard) {
            storageBoard = document.createElement('div');
            storageBoard.id = 'board2';
            storageBoard.className = 'storage-board'; // Add styling class
            document.body.appendChild(storageBoard); // Or append to specific container
        }
        
        // Move element to storage
        const clone = el1.cloneNode(true);
        clone.dataset.originalPosition = el1.dataset.position; // Remember original position
        clone.dataset.storageIndex = j; // Remember the storage index used
        clone.classList.remove("selected");
        
        storageBoard.appendChild(clone);
        
        // Create placeholder for main board
        const placeholder = document.createElement('div');
        placeholder.className = 'placeholder';
        placeholder.dataset.position = el1.dataset.position;
        placeholder.dataset.storageIndex = j;
        placeholder.textContent = `Stored (${j})`;
        
        board.replaceChild(placeholder, el1);
        
        console.log(`Moved element from position ${i} to storage (index ${j})`);
        return;
    }
    
    // Check if i is out of bounds (retrieve from storage)
    if (i >= boardChildren.length || i < 0) {
        const storageBoard = document.getElementById('board2');
        if (!storageBoard) return;
        
        // Find element in storage with matching storageIndex
        const storedElements = storageBoard.children;
        let storedElement = null;
        
        for (let elem of storedElements) {
            if (elem.dataset.storageIndex == i) {
                storedElement = elem;
                break;
            }
        }
        
        if (!storedElement) return;
        
        const el2 = boardChildren[j];
        if (!el2) return;
        
        // Move stored element back to main board
        const clone1 = storedElement.cloneNode(true);
        
        // Restore original position data and clean up storage data
        clone1.dataset.position = el2.dataset.position;
        delete clone1.dataset.originalPosition;
        delete clone1.dataset.storageIndex;
        
        // Handle what happens to el2
        if (el2.classList.contains('placeholder')) {
            // If el2 is a placeholder, just replace it with stored element
            board.replaceChild(clone1, el2);
        } else {
            // If el2 is a real element, move it to storage and create placeholder
            const clone2 = el2.cloneNode(true);
            clone2.dataset.originalPosition = el2.dataset.position;
            clone2.dataset.storageIndex = i;
            
            // Create new placeholder for el2's position
            const placeholder = document.createElement('div');
            placeholder.className = 'placeholder';
            placeholder.dataset.position = el2.dataset.position;
            placeholder.dataset.storageIndex = i;
            placeholder.textContent = `Stored (${i})`;
            
            board.replaceChild(clone1, el2);
            storageBoard.appendChild(clone2);
        }
        
        clone1.classList.remove("selected");
        
        console.log(`Swapped stored element (index ${i}) with position ${j}`);
        return;
    }
    
    // Normal swap operation (both elements exist on main board)
    const el2 = boardChildren[j];
    if (!el1 || !el2 || el1 === el2) return;
    
    // Swap data-position
    const tmpPos = el1.dataset.position;
    el1.dataset.position = el2.dataset.position;
    el2.dataset.position = tmpPos;
    
    // Clone for visual + state reset
    const clone1 = el1.cloneNode(true);
    const clone2 = el2.cloneNode(true);
    
    // Swap in DOM
    board.replaceChild(clone1, el2);
    board.replaceChild(clone2, el1);
    
    // Remove selected class
    clone1.classList.remove("selected");
    clone2.classList.remove("selected");
    
    console.log(`Swapped positions ${i} and ${j}`);
}

// Optional: Helper function to get all stored elements
function getStoredElements() {
    const storageBoard = document.getElementById('board2');
    if (!storageBoard) return [];
    
    return Array.from(storageBoard.children).map(elem => ({
        element: elem,
        storageIndex: elem.dataset.storageIndex,
        originalPosition: elem.dataset.originalPosition
    }));
}

// Optional: Helper function to clear storage
function clearStorage() {
    const storageBoard = document.getElementById('board2');
    if (storageBoard) {
        storageBoard.innerHTML = '';
    }
}


for(let i = 0; i < 144; i++) {
    swap_away(i,1000 + i);
}

function swapMultiplePieces(swapArray) {
    for (const [i, j] of swapArray) {
        swap_away(j + 1000, i);
    }
}

swapMultiplePieces([[142, 114], [100, 42], [47, 93], [135, 30], [124, 6], [13, 52], [75, 49], [99, 116], [134, 11], [0, 107], [117, 27], [49, 39], [25, 36], [120, 5], [63, 53], [21, 48], [48, 24], [15, 86], [33, 133], [34, 77], [18, 101], [125, 23], [104, 87], [139, 78], [68, 4], [110, 19], [129, 17], [143, 115], [101, 103], [52, 60], [79, 106], [141, 126], [46, 7], [73, 3], [43, 40], [103, 20], [62, 94], [1, 76], [66, 63], [27, 100], [65, 74], [19, 118], [51, 18], [32, 44], [123, 142], [140, 90], [131, 91], [29, 32], [74, 111], [112, 61], [92, 34], [119, 9], [58, 132], [91, 15], [54, 22], [89, 80], [31, 41], [111, 102], [59, 58], [42, 14], [35, 50], [80, 59], [88, 56], [40, 131], [121, 128], [39, 124], [132, 0], [24, 97], [45, 139], [86, 81], [71, 125], [122, 51], [133, 28], [69, 21], [136, 54], [8, 37], [28, 141], [12, 83], [44, 2], [64, 69], [128, 45], [118, 98], [56, 31], [98, 109], [84, 35], [96, 62], [10, 57], [126, 112], [97, 71], [127, 95], [9, 66], [14, 1], [113, 85], [6, 38], [37, 8], [22, 79], [90, 16], [53, 99], [50, 130], [41, 113], [106, 82], [137, 120], [108, 55], [77, 12], [82, 67], [7, 143], [85, 13], [5, 73], [55, 46], [138, 137], [30, 123], [87, 33], [72, 68], [94, 110], [4, 134], [78, 135], [38, 65], [20, 140], [76, 64], [93, 29], [116, 25], [105, 70], [26, 105], [115, 127], [107, 136], [11, 92], [2, 88], [60, 26], [109, 72], [3, 47], [102, 104], [17, 108], [83, 119], [67, 121], [81, 75], [70, 117], [130, 129], [57, 89], [23, 84], [16, 96], [61, 122], [114, 138], [95, 10], [36, 43]])

