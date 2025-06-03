##  網格地圖開發
目標：開發一個大小為 nxn 的網格地圖，允許用戶指定維度 'n'（範圍從 5 到9），使用 Flask 網頁應用程式。
功能要求：

用戶可以透過滑鼠點擊指定起始單元格（點擊後顯示為綠色）和結束單元格（點擊後顯示為紅色）。

用戶可以設定 n-2 個障礙物，透過滑鼠點擊將這些單元格變為灰色。


## Prompt:
 write a flask web that takes n as user input n=5 to 9, and generate n x n square.
the layout configuration as follows,
1. Users can specify the starting cell (displayed in green after clicking) and the ending cell (displayed in red after clicking) by clicking the mouse.
2. The user can set n-2 obstacles and turn these cells gray by clicking the mouse. 
3. body and square is aligned center. 
4. the cell width and height is 50px. 
5. the border size is 1px.
6. the cell label is number and aligned center.  
7.Project Directory Structure: 
project/
├── app.py(Flask 後端)
├── templates/
│   ├── index.html(用戶輸入 n 的頁面)
      └── square.html (顯示 n x n 網格並處理點擊事件)

## Response:
Here is the code to implement your Flask web application:

### Directory Structure:

```
project/
├── app.py
├── templates/
│   ├── index.html
│   └── square.html
```

### `app.py` (Flask Backend):

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_square', methods=['POST'])
def generate_square():
    n = int(request.form.get('n'))
    return render_template('square.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html` (User Input Page):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Size Input</title>
</head>
<body>
    <h2>Enter a value for n (5 to 9)</h2>
    <form method="POST" action="/generate_square">
        <label for="n">n (5 to 9):</label>
        <input type="number" id="n" name="n" min="5" max="9" required>
        <button type="submit">Generate Grid</button>
    </form>
</body>
</html>
```

### `templates/square.html` (Grid Page):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ n }} x {{ n }} Grid</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            flex-direction: column;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat({{ n }}, 50px);
            grid-template-rows: repeat({{ n }}, 50px);
            gap: 1px;
        }
        .cell {
            width: 50px;
            height: 50px;
            border: 1px solid black;
            text-align: center;
            line-height: 50px;
            cursor: pointer;
        }
        .start {
            background-color: green;
        }
        .end {
            background-color: red;
        }
        .obstacle {
            background-color: gray;
        }
    </style>
</head>
<body>

    <h2>{{ n }} x {{ n }} Grid</h2>
    <div class="grid" id="grid">
        {% for i in range(n) %}
            {% for j in range(n) %}
                <div class="cell" data-x="{{ i }}" data-y="{{ j }}" onclick="cellClick(event)">
                    {{ i * n + j + 1 }}
                </div>
            {% endfor %}
        {% endfor %}
    </div>

    <p>Click on a cell to set:</p>
    <ul>
        <li><strong>STEP1:</strong> One start cell to green</li>
        <li><strong>STEP2:</strong> One end cell to red</li>
        <li><strong>STEP3:</strong> n-2 wall blocked cell to gray</li>
    </ul>

    <script>
        let startCell = null;
        let endCell = null;
        let obstacles = 0;

        function cellClick(event) {
            const cell = event.target;
            const x = parseInt(cell.getAttribute('data-x'));
            const y = parseInt(cell.getAttribute('data-y'));

            if (!startCell) {
                startCell = cell;
                cell.classList.add('start');
            } else if (!endCell) {
                endCell = cell;
                cell.classList.add('end');
            } else if (obstacles < {{ n }} - 2) {
                cell.classList.add('obstacle');
                obstacles++;
            }

            // Prevent starting and ending cells from being obstacles
            if (cell === startCell || cell === endCell) {
                cell.classList.remove('obstacle');
            }
        }
    </script>

</body>
</html>

```

### Explanation:

1.  **app.py**:
    
    *   The main Flask application serves two routes:
        
        *   `/`: Displays a simple input form where users can enter a number `n` between 5 and 9.
            
        *   `/generate_square`: Accepts the form data (the value of `n`) and renders a page displaying a `n x n` grid.
            
2.  **index.html**:
    
    *   A form for users to input the value of `n`, with validation ensuring that `n` is between 5 and 9.
        
    *   The form submits the input to `/generate_square` to generate the grid.
        
3.  **square.html**:
    
    *   This page displays a `n x n` grid where each cell is clickable.
        
    *   The grid is generated dynamically using Jinja templating based on the value of `n` passed from the backend.
        
    *   Users can click cells to set a starting cell (green), an ending cell (red), and obstacles (gray).
        
    *   JavaScript functions handle the click events and prevent cells from being both the start/end and obstacles simultaneously.
        

### Running the Application:

1.  Navigate to the project folder and run `app.py`:
    
    ```bash
    python app.py
    ```
    
2.  Open your browser and go to `http://127.0.0.1:5000/` to use the web application.
    

You should now be able to input a number for `n`, generate the `n x n` grid, and interact with it by clicking to set the starting cell, ending cell, and obstacles.

