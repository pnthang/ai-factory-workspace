To create a Todo app using Node.js, React.js, and PostgreSQL, we'll need to make changes across multiple files. Here's a step-by-step guide on what changes to make:

**Step 1: Create the Server-Side API (Node.js)**

Create a new file at `workspace/server/api.js` with the following content:
```javascript
// api.js
const express = require('express');
const app = express();
const port = process.env.PORT || 3001;

app.use(express.json());

const db = require('./db');

app.get('/api/todos', async (req, res) => {
  try {
    const todos = await db.query('SELECT * FROM todos');
    res.json(todos);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.post('/api/todos', async (req, res) => {
  try {
    const { text } = req.body;
    await db.query(`INSERT INTO todos (text) VALUES ($1)`, [text]);
    res.status(201).send({ message: 'Todo created successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.put('/api/todos/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { text } = req.body;
    await db.query(`UPDATE todos SET text=$1 WHERE id=$2`, [text, id]);
    res.status(200).send({ message: 'Todo updated successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.delete('/api/todos/:id', async (req, res) => {
  try {
    const { id } = req.params;
    await db.query(`DELETE FROM todos WHERE id=$1`, [id]);
    res.status(200).send({ message: 'Todo deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
This file sets up an Express.js API with routes for retrieving, creating, updating, and deleting Todo items. It also imports the `db` module from a separate file (`workspace/server/db.js`) that will handle database connections.

**Step 2: Create the Database Connection (PostgreSQL)**

Create a new file at `workspace/server/db.js` with the following content:
```javascript
// db.js
const { Pool } = require('pg');

const pool = new Pool({
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

module.exports = pool;
```
Replace the placeholders with your actual PostgreSQL credentials.

**Step 3: Create the Frontend (React.js)**

Create a new file at `workspace/client/App.js` with the following content:
```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editing, setEditing] = useState(null);

  useEffect(() => {
    axios.get('/api/todos')
      .then(response => {
        setTodos(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleAddTodo = () => {
    if (newTodo) {
      axios.post('/api/todos', { text: newTodo })
        .then(response => {
          setTodos([...todos, response.data]);
          setNewTodo('');
        })
        .catch(error => {
          console.error(error);
        });
    }
  };

  const handleEditTodo = todoId => {
    setEditing(todoId);
  };

  const handleUpdateTodo = () => {
    if (editing) {
      axios.put(`/api/todos/${editing}`, { text: newTodo })
        .then(response => {
          setTodos(todos.map(todo => (todo.id === editing ? response.data : todo)));
          setEditing(null);
          setNewTodo('');
        })
        .catch(error => {
          console.error(error);
        });
    }
  };

  const handleDeleteTodo = todoId => {
    axios.delete(`/api/todos/${todoId}`)
      .then(() => {
        setTodos(todos.filter(todo => todo.id !== todoId));
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Todo List</h1>
      <form>
        <input
          type="text"
          value={newTodo}
          onChange={e => setNewTodo(e.target.value)}
          placeholder="Enter new todo"
        />
        <button onClick={handleAddTodo}>Add Todo</button>
      </form>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {editing === todo.id ? (
              <input
                type="text"
                value={newTodo}
                onChange={e => setNewTodo(e.target.value)}
                placeholder="Edit Todo"
              />
            ) : (
              <span>{todo.text}</span>
            )}
            {editing !== todo.id && (
              <button onClick={() => handleEditTodo(todo.id)}>Edit</button>
            )}
            {editing === null || editing !== todo.id && (
              <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```
This file sets up a React app with a Todo list, allowing users to add, edit, and delete items. It uses the `axios` library to make API calls to our Node.js server.

**Step 4: Start the Server**

Create a new file at `workspace/server/index.js` with the following content:
```javascript
// index.js
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use('/api', require('./api'));

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
This file sets up an Express.js server that serves our API at the `/api` route.

**Step 5: Start the Client**

Create a new file at `workspace/client/index.js` with the following content:
```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```
This file sets up our React app to render the `App` component in an HTML element with the ID `root`.

That's it! You now have a Todo app using Node.js, React.js, and PostgreSQL.