import React from 'react';
import first from './photos/first.jpg'
import second from './photos/second.jpg'
import third from './photos/third.jpg'
import fourth from './photos/fourth.jpg'
import fifth from './photos/fifth.jpg'
import sixth from './photos/sixth.jpg'
import seventh from './photos/seventh.jpg'
import eighth from './photos/eighth.jpg'
import nineth from './photos/nineth.jpg'
import tenth from './photos/tenth.jpg'

const HomePage = () => {
  console.log('this is recipe home page');
  return (
    <div > 
      <table>
        <tr>
          <td><img src={first} alt="first image"/></td>
          <td><img src={second} alt="second image"/></td>
          <td><img src={third} alt="third image"/></td>
          <td><img src={fourth} alt="fourth image"/></td>
          <td><img src={fifth} alt="fifth image"/></td>
        </tr>  
        <tr>
          <td><img src={sixth} alt="sixth image"/></td>
          <td><img src={seventh} alt="seventh image"/></td>
          <td><img src={eighth} alt="eighth image"/></td>
          <td><img src={nineth} alt="nineth image"/></td>
          <td><img src={tenth} alt="tenth image"/></td>
        </tr>
      </table>
        
    </div>
  );
};

export default HomePage;
