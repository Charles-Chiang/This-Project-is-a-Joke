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
              <input type="text" className="form-control" placeholder="Noun #1"></input>
            </div>
            <div className="col-sm">
              <input type="text" className="form-control" placeholder="Noun #2"></input>
            </div>
            <div className="col-sm"></div>
          </div>
        </div>

        <div className="form-group">
        <div className="row">
            <div className="col-sm"></div>
            <div className="col-sm">
              <select class="custom-select my-2" id="selectNounType">
                <option selected>Choose type...</option>
                <option value="1">Person</option>
                <option value="2">Place</option>
                <option value="3">Event</option>
                <option value="4">Thing</option>
              </select>
            </div>
            <div className="col-sm">
              <select class="custom-select my-2" id="selectNounType">
                <option selected>Choose type...</option>
                <option value="1">Person</option>
                <option value="2">Place</option>
                <option value="3">Event</option>
                <option value="4">Thing</option>
              </select>
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
