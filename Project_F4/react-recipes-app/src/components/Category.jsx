import React, {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import axios from "axios";


function Category(props) {

    const cat = useParams().category;

    const [isLoading, setLoading] = useState(true);
    const [recipes, setRecipe] = useState();


    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/recipes/").then(res => {
        console.log(res);
            setRecipe(res.data);
            setLoading(false);
        });

    }, []);

    if (isLoading) {
        return <h1>Loading...</h1>;
    }

    return (
        <div>
            <h1>{cat}:</h1>
            <div className='recipe'>
                {recipes.filter(recipe => recipe.category === cat).map((name) => (
                <p key={name.id}><a className="r" href={`/recipe/${name.id}`}>{name.title}</a></p>
                ))}
            </div>
        </div>
    );
};

export default Category;