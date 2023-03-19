import React, {useState, useEffect} from 'react';
import Card from './Card.js';

export const Home = ()=> {

    const [name, fname] = useState([])

    useEffect(()=> {
        fetch('/home').then(response => {
            if(response.ok){
                return response.json().then(data => console.log(data))
            }
        })
    }, [])

    return(
        <>
            <Card/>
        </>
    )
}
export default Home