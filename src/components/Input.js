import { useState } from "react";
import Network from './Network'
import getMentions from '../api'
function Input(){
    const [name, setName] = useState("")
    const [mentionData, setMentionData] = useState(null)
    const [loading, setLoading] = useState(false)

    const submit = (e) => {
        e.preventDefault();

        if( name !== ''){
            setLoading(true)
            setMentionData(null)
            getMentions(name).then( (res) =>{
                
                setMentionData(res.data)
                setLoading(false)
            
            })
        }
        
    }

    return(
        <div class="ui container">
            <div class="ui grid">
                <div class="sixteen wide column centered">
                
                    <div class="ui fluid card">
                        <div class="content">
                            <div class="header">Analyse your Twitter network</div>
                            <div class="description">
                                Please enter your username.
                            </div>
                            <br/>
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
                                <button class="ui button" type="submit"><i class="add icon"></i>Submit</button>
                                {
                                    loading && <div class='ui active inline small loader'></div>
                                }
                            </form>    
                        </div>
                    </div>    

                </div>
                
            </div>
            { mentionData && 
                <div class="ui grid">
                    <div class="sixteen wide column centered">
                        <div class="ui fluid card">
                            <div class="content">
                                <Network data={mentionData}/>
                            </div>
                        </div>
                    </div>
                </div>
            }
            
        </div>    
    );
}


export default Input;