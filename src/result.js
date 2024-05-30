import './result.css';
 import logo from './Logo2.png';
//import {useState} from 'react';

function SearchBar(props)
{
    // 검색창 부분
    return (
        <div id="searchbar">
            <form onSubmit={event=>{
                event.preventDefault();
                const search = event.target.search.value;
                props.onCreate(search);
            }}>
                <p><input type="text" name="search" placeholder="Search..." onkeypress="if(event.keycode ==13){Search();}"/></p>
            </form>
        </div>
)
}

function LogoImage()
{
    // 이미지 버튼 -> 메인화면으로 넘어가기
    return (
        <div id="logo">
            <img src={logo}
            className="Result-logo"
            alt="logo"
            onclick={()=>{
                // 메인 화면으로 이동
            }}/>
        </div>
)
}

function ObjectionButton()
{
    return (
        <div id="objection">
            <button
            onclick={event=>{
                event.preventDefault();
                event.Create();
                //이의신청 하기
            }}>이의신청</button>
        </div>
    )
}
function Create(props){
    return <article>
      <form onSubmit={event=>{
        event.preventDefault();
        const title = event.target.title.value;
        const body = event.target.body.value;
        props.onCreate(title,body);
      }}>
        <p><input type="text" name="title" placeholder="title"/></p>
        <p><textarea name="body" placeholder='body'></textarea></p>
        <p><input type="submit" value="Create"></input></p>
      </form>
    </article>
  }

// function Objection()
// {

// }


function ResultBox()
{
    return (
        <div id="resultBox">
            <div class="link">https://www.youtube.com</div>
            <br></br>
            <div class="description">
                <p>
                    <span class="span">
                        사이트명 : Youtube
                        <br></br>
                        <br></br>
                        피싱 사이트 여부 :
                    </span>
                    <span> 피싱 사이트가 아님</span>
                </p>
            </div>
        </div>
    )
}

function SideBar()
{
    return(
        <div id="left">
            <div class="black-list">
            <hr></hr>
                <a href>Black List</a>
                <p class="element">
                    블랙리스트를 확인할 수 있는 게시판
                    <br></br>
                    현재 등록된 사이트 : 14,042개
                    {/* 값 변경할 수 있도록 처리 */}
                </p>
                <hr></hr>
                <hr></hr>
            </div>
            <div class="white-list">
                <a href>White List</a>
                <p class="element">
                    화이트리스트를 확인할 수 있는 게시판
                    <br></br>
                    현재 등록된 사이트 : 240,410개
                </p>
                <hr></hr>
            </div>
        </div>
    )
}

function Result()
{
    return (
        <div>
            <div id="top">
                <LogoImage></LogoImage>
                {/* 실제로 화면에 보이는 부분 */}
                <SearchBar></SearchBar> 
                {/* 검색창 부분 */}
            </div>
            <br></br>
            <br></br>
            <br></br>

            {/* 이 부분 추후에 수정하기 */}
            <SideBar></SideBar>
            <ResultBox></ResultBox>
            <ObjectionButton></ObjectionButton>
        </div>
    );
}

export default Result;