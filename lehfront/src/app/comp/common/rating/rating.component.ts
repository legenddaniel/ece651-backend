import { Component } from '@angular/core';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html'
})
export class RatingComponent {
  selected = 4;
  hovered = 0;
  readonly = false;

}
