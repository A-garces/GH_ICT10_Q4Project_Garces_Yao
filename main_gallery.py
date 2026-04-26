import numpy as np
from pyscript import document

photos = np.array([
["1.jpg","December 18, 2025","Christmas Party"],
["2.jpg","April 21, 2026","CAT Graduation/President Day"],
["3.jpg","December 5, 2025","Food Fair and Minimart"],
["4.jpg","January 13-14, 2026","GH Girls Joint Camp Out"]
])

gallery = document.getElementById("gallery")

cards = ""

for photo in photos:
    cards += f"""
    <div class='card m-3' style='width:18rem; display:inline-block; border-radius: 20px;'>
        <img src='{photo[0]}' class='card-img-top'>
        <div class='card-body'>
            <h5>{photo[1]}</h5>
            <p>{photo[2]}</p>
        </div>
    </div>
    """

gallery.innerHTML = cards