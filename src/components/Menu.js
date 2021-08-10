import logo from '../logo.png'

function Menu() {
  return (
      <div class="ui attached menu">
        <div class="ui container">
          <a class="left item">
            <img src={logo} style={{width: '50px', height: '50px'}} alt="My logo" />
          </a>
          <a class="right item">
            <i class="twitter icon"></i> @twitterusername 
          </a>
          
          
        </div>
      </div>
  );
}

export default Menu;
