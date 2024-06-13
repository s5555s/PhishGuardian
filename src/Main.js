import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Main.css';
import logo from './Logo.png';

function Header() {
    return (
        <header>
            <img src={logo} className="Main-logo" alt="logo" />
        </header>
    );
}

function Create({ onCreate }) {
    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        const search = event.target.search.value;
        onCreate(search);
        navigate('/result', { state: { url: search } });
    };

    return (
        <form onSubmit={handleSubmit}>
            <p><input type="text" name="search" placeholder="Search..." /></p>
        </form>
    );
}

function Main() {
    return (
        <div>
            <Header />
            <Create onCreate={(url) => console.log(url)} />
        </div>
    );
}

export default Main;

