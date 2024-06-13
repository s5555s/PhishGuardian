import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import './result.css';
import logo from './Logo2.png';

function SearchBar({ onSearch }) {
    return (
        <div id="searchbar">
            <form onSubmit={event => {
                event.preventDefault();
                const search = event.target.search.value;
                onSearch(search);
            }}>
                <p><input type="text" name="search" placeholder="Search..." /></p>
            </form>
        </div>
    );
}

function LogoImage() {
    return (
        <div id="logo">
            <img src={logo} className="Result-logo" alt="logo" onClick={() => {
                // 메인 화면으로 이동
            }}/>
        </div>
    );
}

function ObjectionButton() {
    return (
        <div id="objection">
            <button onClick={event => {
                event.preventDefault();
                // 이의신청 하기
            }}>이의신청</button>
        </div>
    );
}

function ResultBox({ result }) {
    return (
        <div id="resultBox">
            <div className="link">{result.url}</div>
            <br />
            <div className="description">
                <p>
                    <span className="span">
                        사이트명 : {result.url}
                        <br />
                        <br />
                        피싱 사이트 여부 :
                    </span>
                    <span> {result.result === 'Phishing' ? '피싱 사이트' : '피싱 사이트가 아님'}</span>
                </p>
            </div>
        </div>
    );
}

function SideBar() {
    return (
        <div id="left">
            <div className="black-list">
                <hr />
                <a href="#">Black List</a>
                <p className="element">
                    블랙리스트를 확인할 수 있는 게시판
                    <br />
                    현재 등록된 사이트 : 14,042개
                </p>
                <hr />
            </div>
            <div className="white-list">
                <a href="#">White List</a>
                <p className="element">
                    화이트리스트를 확인할 수 있는 게시판
                    <br />
                    현재 등록된 사이트 : 240,410개
                </p>
                <hr />
            </div>
        </div>
    );
}

function Result() {
    const location = useLocation();
    const [result, setResult] = useState(null);

    useEffect(() => {
        const url = location.state?.url;
        if (url) {
            const fetchData = async () => {
                try {
                    const response = await axios.post('http://13.124.175.42:5001/predict', { url });
                    if (response.status === 200) {
                        setResult({ url: url, result: response.data.result });
                    }
                } catch (error) {
                    console.error('Error fetching data from server', error);
                }
            };
            fetchData();
        }
    }, [location.state]);

    return (
        <div>
            <div id="top">
                <LogoImage />
                <SearchBar onSearch={(url) => setResult({ url, result: '검색 중...' })} />
            </div>
            <br />
            <SideBar />
            {result && <ResultBox result={result} />}
            <ObjectionButton />
        </div>
    );
}

export default Result;

