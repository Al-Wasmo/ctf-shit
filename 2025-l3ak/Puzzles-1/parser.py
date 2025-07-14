import json
import base64
from PIL import Image
import io
import numpy as np
import random


def split_image_to_dict(img,size):
    width, height = img.size
    tile_width = width // size
    tile_height = height // size

    tiles = {}

    for y in range(size):
        for x in range(size):
            left = x * tile_width
            upper = y * tile_height
            right = left + tile_width
            lower = upper + tile_height

            tile = img.crop((left, upper, right, lower))

            # Save tile to bytes buffer
            buffer = io.BytesIO()
            tile.save(buffer, format='PNG')
            encoded = base64.b64encode(buffer.getvalue()).decode('utf-8')

            # Store with position
            tiles[(x, y)] = encoded

    return tiles


def reorder_random_target_matching(splited, pieces, size=12):
    def decode_img(b64):
        return Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")

    def mse_score(img1, img2, pad=2):
        # Crop padding from all sides
        cropped1 = img1.crop((pad, pad, img1.width - pad, img1.height - pad))
        cropped2 = img2.crop((pad, pad, img2.width - pad, img2.height - pad))

        arr1 = np.array(cropped1).astype(np.float32)
        arr2 = np.array(cropped2).astype(np.float32)

        return np.mean((arr1 - arr2) ** 2)

    # Decode everything
    splited_imgs = {pos: decode_img(b64) for pos, b64 in splited.items()}
    piece_imgs = [decode_img(b64) for b64 in pieces]

    available_tiles = list(splited_imgs.keys())
    used_pieces = [False] * len(pieces)
    ordered = [None] * (size * size)

    ordered_index = []

    while available_tiles:
        # Pick a random target tile position
        pos = random.choice(available_tiles)
        available_tiles.remove(pos)

        target_img = splited_imgs[pos]

        # Find best unused piece
        best_score = float("inf")
        best_index = -1

        for i, candidate_img in enumerate(piece_imgs):
            if used_pieces[i]:
                continue
            score = mse_score(target_img, candidate_img)
            if score < best_score:
                best_score = score
                best_index = i

        if best_index == -1:
            raise RuntimeError("Ran out of pieces!")

        used_pieces[best_index] = True
        x, y = pos
        idx = y * size + x
        ordered[idx] = pieces[best_index]
        ordered_index.append([idx,best_index])

    return ordered_index, ordered  # ordered[y * size + x]

def decode_img(b64):
    return Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")

def reconstruct_image(ordered_pieces, tile_width,tile_height, output_path,size):
    full_img = Image.new("RGB", (size * tile_width, size * tile_height))

    for idx, b64 in enumerate(ordered_pieces):
        tile = decode_img(b64)
        x = (idx % size) * tile_width
        y = (idx // size) * tile_height
        full_img.paste(tile, (x, y))

    full_img.save(output_path)

data = ""
with open("file.json","rb") as f:
    data = json.loads(f.read())

puzzle_id = data["puzzle_id"]
width = data["width"]
height = data["height"]
cols = data["cols"]
rows = data["rows"]
title = data["title"]



img = Image.open(title + ".jpeg")
resized_img = img.resize((cols * width, rows * height))


pieces = data["pieces"]
# reconstruct_image(pieces,decode_img(pieces[0]).size[0],decode_img(pieces[0]).size[1],"output.png",12)
# exit()

splited = split_image_to_dict(resized_img,rows)

ordered_indexs, ordered = reorder_random_target_matching(splited,pieces,size=rows)
reconstruct_image(ordered,decode_img(ordered[0]).size[0],decode_img(ordered[0]).size[1],"output.png",12)

print(f"""
function swap_away(i, j) {"{"}
    const boardChildren = board.children;
    const el1 = boardChildren[i];
    
    // Check if j is out of bounds (storage operation)
    if (j >= boardChildren.length || j < 0) {"{"}
        if (!el1) return; // Can't move non-existent element
        
        // Create storage board if it doesn't exist
        let storageBoard = document.getElementById('board2');
        if (!storageBoard) {"{"}
            storageBoard = document.createElement('div');
            storageBoard.id = 'board2';
            storageBoard.className = 'storage-board'; // Add styling class
            document.body.appendChild(storageBoard); // Or append to specific container
        {"}"}
        
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
        placeholder.textContent = `Stored {"(${"}j{"}"})`;
        
        board.replaceChild(placeholder, el1);
        
        console.log(`Moved element from position {"${"}i{"}"} to storage (index {"${"}j{"}"})`);
        return;
    {"}"}
    
    // Check if i is out of bounds (retrieve from storage)
    if (i >= boardChildren.length || i < 0) {"{"}
        const storageBoard = document.getElementById('board2');
        if (!storageBoard) return;
        
        // Find element in storage with matching storageIndex
        const storedElements = storageBoard.children;
        let storedElement = null;
        
        for (let elem of storedElements) {"{"}
            if (elem.dataset.storageIndex == i) {"{"}
                storedElement = elem;
                break;
            {"}"}
        {"}"}
        
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
        if (el2.classList.contains('placeholder')) {"{"}
            // If el2 is a placeholder, just replace it with stored element
            board.replaceChild(clone1, el2);
        {"}"} else {"{"}
            // If el2 is a real element, move it to storage and create placeholder
            const clone2 = el2.cloneNode(true);
            clone2.dataset.originalPosition = el2.dataset.position;
            clone2.dataset.storageIndex = i;
            
            // Create new placeholder for el2's position
            const placeholder = document.createElement('div');
            placeholder.className = 'placeholder';
            placeholder.dataset.position = el2.dataset.position;
            placeholder.dataset.storageIndex = i;
            placeholder.textContent = `Stored {"(${"}i{"}"})`;
            
            board.replaceChild(clone1, el2);
            storageBoard.appendChild(clone2);
        {"}"}
        
        clone1.classList.remove("selected");
        
        console.log(`Swapped stored element (index {"${"}i{"}"}) with position {"${"}j{"}"}`);
        return;
    {"}"}
    
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
    
    console.log(`Swapped positions {"${"}i{"}"} and {"${"}j{"}"}`);
{"}"}

// Optional: Helper function to get all stored elements
function getStoredElements() {"{"}
    const storageBoard = document.getElementById('board2');
    if (!storageBoard) return [];
    
    return Array.from(storageBoard.children).map(elem => {"({"}
        element: elem,
        storageIndex: elem.dataset.storageIndex,
        originalPosition: elem.dataset.originalPosition
    {"}"}));
{"}"}

// Optional: Helper function to clear storage
function clearStorage() {"{"}
    const storageBoard = document.getElementById('board2');
    if (storageBoard) {"{"}
        storageBoard.innerHTML = '';
    {"}"}
{"}"}


for(let i = 0; i < 144; i++) {"{"}
    swap_away(i,1000 + i);
{"}"}

function swapMultiplePieces(swapArray) {"{"}
    for (const [i, j] of swapArray) {"{"}
        swap_away(j + 1000, i);
    {"}"}
{"}"}

swapMultiplePieces({ordered_indexs})
""")


