import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <p>Humoroo!</p>
      <form>
        <div class="row">
          <div class="col-2">
            <input type="text" class="form-control" placeholder="Word #1"></input>
          </div>
          <div class="col-2">
            <input type="text" class="form-control" placeholder="Word #2"></input>
          </div>
        </div>
      </form>
    </div>
  );
}

export default App;
