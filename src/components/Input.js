import { useState } from "react";
import data from '../data/data-1.json'


function Input(){
    const [name, setName] = useState("")
    const [show, setShow] = useState(false)


    const submit = (e) => {
        e.preventDefault();
        alert(`Your user name is: ${name}`)
    }

    return(
        <div class="ui container">
            <div class="ui grid">
                <div class="ten wide column">
                
                    <div class="ui fluid card">
                        <div class="content">
                            <div class="header">Analyse your Twitter network</div>
                            <div class="description">
                                Please enter your username.
                            </div>

                            <form class="ui form" onSubmit={submit}>
                                <div class="field">
                                    <div class="ui labeled fluid icon input">
                                    <div class="ui label">
                                      @
                                    </div>
                                          <input type="text" placeholder="Username..." value={name} onChange={e => setName(e.target.value)}/>
                                          <i class="search icon"></i>
                                    </div>
                                </div>
                                <button class="ui button" type="submit"><i class="add icon"></i>Add</button>
                            </form>          
                    
                        </div>
                    </div>    

                </div>
                
            </div>
            <div class="ui grid">
                <div class="ten wide column">
                    <div class="ui fluid card">
                        <div class="content">
                            
                            <div class="ui centered card">
                              <div class="image">
                                <img src={data.pic}/>
                              </div>
                              <div class="content">
                                <a class="header">{data.name}</a>
                              </div>
                            </div>
                            <div class="ui three stackable cards">
                                {data.mentions.map(
                                    (mention,key) => {

                                        return(
                                            <div key={key} class="card">
                                                <div class="image">
                                                    <img src={mention.pic}/>
                                                </div>
                                                <div class="content">
                                                    <a class="header">{mention.name}</a>

                                                    {mention.mentions.map((m, key) =>
                                                        <li key={key}> {m.name}</li>
                                                    )}
                                                </div>
                                            </div>
                                        )
                                    }

                                )}
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
    );
}


export default Input;