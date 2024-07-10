import Review from '../reusable/Reviews.js';
import './reviews.css';

const Reviews = () => {
  return (
    <div className='reviewsBoxContainer'>
      <Review movieName='Fast and Furious 1' stars={2.5} />
      <Review movieName='Fast and Furious 2' stars={5} />
      <Review movieName='Fast and Furious 3' stars={3.5} />
      <Review movieName='Fast and Furious 4' stars={4.5} />
      <Review movieName='Fast and Furious 5' stars={5} />
    </div>
  );
};
export default Reviews;
