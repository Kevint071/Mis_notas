import React, { useState} from "react";
import "../../Styles/Menu/style_menu.css";
import ListaMenu from "./ListaMenu";
import {IoIosArrowDropdownCircle} from "react-icons/io";


function MenuPython() {
  const [showMenu, setShowMenu] = useState(null);

  const handleClick = (id) => {
    setShowMenu(showMenu == id ? null : id)
  }
  // style={showMenu ? {display: "block"} : {display: "none"}}
  return (
    <div id="menu_python">
      <div id="menu">
        <ul>
          {ListaMenu.map((item) => (
            <li key={item.id} className="menu-item">
              <a href="#" onClick={() => handleClick(item.id)}>
                {item.title} <IoIosArrowDropdownCircle style={{float: "right"}}/>
              </a>
              {showMenu === item.id ? <>{item.content}</> : null}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default MenuPython;