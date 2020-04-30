<template>
	<div class="container col-sm-4 col-md-7 col-lg-4 mt-5">
		<div class="card">
			<h3 class="card-header text-center">
				{{ this.months[this.currentMonth] + " " + this.currentYear }}
			</h3>
			<table
				class="table table-bordered table-responsive-sm"
				id="calendar"
				ref="calendar"
			>
				<thead>
					<tr>
						<th>Sun</th>
						<th>Mon</th>
						<th>Tue</th>
						<th>Wed</th>
						<th>Thu</th>
						<th>Fri</th>
						<th>Sat</th>
					</tr>
				</thead>

				<tbody ref="calendar-body">
					<!--the table will be generated here-->
				</tbody>
			</table>

			<div class="form-inline">
				<button
					class="btn btn-outline-primary col"
					id="previous"
					ref="previous"
					@click="previous()"
				>
					Previous Month
				</button>

				<button
					class="btn btn-outline-primary col"
					id="next"
					ref="next"
					@click="next()"
				>
					Next Month
				</button>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "Calendar",
	mounted() {
		// upon component being mounted show the calendar:
		this.calendar(this.currentMonth, this.currentYear);
	},

	data() {
		return {
			currentMonth: new Date().getMonth(),
			currentYear: new Date().getFullYear()
		};
	},

	computed: {
		months() {
			return [
				"January",
				"February",
				"March",
				"April",
				"May",
				"June",
				"July",
				"August",
				"September",
				"October",
				"November",
				"December"
			];
		}
	},

	methods: {
		/**
		 * Get the next month.
		 */
		next() {
			this.currentYear =
				this.currentMonth === 11
					? this.currentYear + 1
					: this.currentYear;
			this.currentMonth = (this.currentMonth + 1) % 12;

			this.calendar(this.currentMonth, this.currentYear);
		},

		/**
		 * Get the previous month.
		 */
		previous() {
			this.currentYear =
				this.currentMonth === 0
					? this.currentYear - 1
					: this.currentYear;
			this.currentMonth =
				this.currentMonth === 0 ? 11 : this.currentMonth - 1;

			this.calendar(this.currentMonth, this.currentYear);
		},

		/**
		 * Tried to make a table with JavaScript
		 * Alternative approach could be HTML Table
		 * element and looping through it.
		 *
		 * @param month
		 * @param year
		 */
		calendar(month, year) {
			let firstDay = new Date(year, month).getDay();
			// Special way to calculate days in a month
			let daysInMonth = 32 - new Date(year, month, 32).getDate();

			// Get the body of the calendar
			let tbl = this.$refs["calendar-body"];

			// clearing all previous cells
			tbl.innerHTML = "";

			// creating all cells
			let date = 1;
			for (let i = 0; i < 6; i++) {
				// because we need max 6 rows
				// creates a table row
				let row = document.createElement("tr");

				// creating individual cells, filing them up with data.
				for (let j = 0; j < 7; j++) {
					if (i === 0 && j < firstDay) {
						let cell = document.createElement("td");
						let cellText = document.createTextNode("");
						cell.appendChild(cellText);
						row.appendChild(cell);
					} else if (date > daysInMonth) {
						break;
					} else {
						let cell = document.createElement("td");
						let cellText = document.createTextNode(date.toString());
						// START: highlight today's date
						if (
							date === new Date().getDate() &&
							year === new Date().getFullYear() &&
							month === new Date().getMonth()
						) {
							cell.classList.add("bg-primary", "text-white");
						} // END: highlight today's date
						cell.appendChild(cellText);
						row.appendChild(cell);
						date++;
					}
				}

				tbl.appendChild(row); // appending each row into calendar body.
			}
		}
	}
};
</script>
