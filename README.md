# tbcacad_asgmt_three-მესამე დავალება

პროგრამა ტვირთავს 77 JSON ფორმატის მონაცემს და წერს ერთ ფაილში.
ამას აკეთებს რაც შეიძლება სწრაფად threading ბიბლიოთეკის გამოყენებით.
ალტერნატივაა concurrent.futures ბიბლიოთეკაც. ფაილთან მუშაობა არის
threadsafe threading.Lock-ის გამოყენების გამო.

## გამოყენებული მოდულები და ბიბლიოთეკები
* threading
* requests
* concurrent.futures
* time
* json