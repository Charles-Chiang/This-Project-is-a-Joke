import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <p>Humoroo!</p>
      <form>
        <div class="row">
          <div class="col-sm"></div>
          <div class="col-sm">
            <input type="text" class="form-control" placeholder="Word #1"></input>
          </div>
          <div class="col-sm">
            <input type="text" class="form-control" placeholder="Word #2"></input>
          </div>
          <div class="col-sm"></div>
        </div>
      </form>
    </div>
  );
}

export default App;
