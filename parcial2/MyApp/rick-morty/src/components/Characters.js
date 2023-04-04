export default function Characters(props){
    const {characters, setCharacters}=props;

    const resetCharacters = () => {
        setCharacters(null);
    };

    return(
     <div classname="characters">
        <h1 className="text-grey">Personajes</h1>
        <spam className="back-home" onClick={resetCharacters}>Volver a la home</spam>
        <div className="container-characters">
            {characters.map((character, index)=>(
                <div className="character-container" key={index}>
                    <div>
                        <img src={character.image} alt={character.name}/>
                    </div>
                    <div>
                        <h3>{character.name}</h3>
                        <h6>
                            {character.status === 'Alive'?(
                                <>
                                    <spam className="alive"/>
                                    Alive
                                </>
                            ):(
                                <>
                                    <spam className='dead'/>
                                    Dead
                                </>
                            )}
                        </h6>
                        <p>
                            <span className="text-grey">Episodios: </span>
                            <span>{character.episode.length}</span>
                        </p>
                        <p>
                            <span className="text-grey">Especie: </span>
                            <spam>{character.species}</spam>
                        </p>
                    </div>
                </div>
            ))}
        </div>
        <span className="back-home" onClick={resetCharacters}>volver a la home</span>
     </div>
    );
}