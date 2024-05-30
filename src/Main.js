import './Main.css';
import logo from './Logo.png';

function Header()
{
    // 헤더 부분
    return <header>
        <img src={logo}
        className="Main-logo"
        alt="logo"/>
    </header>
}

function Search()
{
    // 입력한 주소를 처리하는 부분
}
function Create(props)
{
    // 검색창 부분
    return <form onSubmit={event=>{
        event.preventDefault();
        const search = event.target.search.value;
        props.onCreate(search);
    }}>
        <p><input type="text" name="search" placeholder="Search..." onkeypress="if(event.keycode ==13){Search();}"/></p>
    </form>
}

function Main()
{
    return (
        <div>
            <Header></Header>   
            {/* 로고가 들어갈 부분 */}
            <Create></Create>   
            {/* 검색창 부분 */}
        </div>
    );
}

export default Main;