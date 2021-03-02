import { useState } from "react";



function Input(){
    const [name, setName] = useState("")

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
        </div>    
    );
}
export default Input;