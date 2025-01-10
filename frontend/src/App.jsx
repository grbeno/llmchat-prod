import './App.css';
import { Link } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <h1> Hello World </h1>
      <br />
      <h2><Link to={window.location.href + "ws/chat"}>AI/LLM Chat</Link></h2>
    </div>
  );
}

export default App;
