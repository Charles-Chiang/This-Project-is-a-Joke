import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <img src="/humoroo_logo_cropped.jpg" alt="image" width="50%"/>
      <form>
        <div className="form-group" id="word-input">
          <div className="row">
            <div className="col-sm"></div>
            <div className="col-sm">
              <input type="text" className="form-control" placeholder="Word #1"></input>
            </div>
            <div className="col-sm">
              <input type="text" className="form-control" placeholder="Word #2"></input>
            </div>
            <div className="col-sm"></div>
          </div>
        </div>
        
        <button type="submit" className="btn btn-info" id="generate">Generate</button>
      </form>
    </div>
  );
}

export default App;
