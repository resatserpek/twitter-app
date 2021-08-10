
function Cards(){
    
    return (       
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
                 
    )
}
export default Cards;