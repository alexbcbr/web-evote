<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  <section id="about" class="section">
    <div class="container">
      <div class="row">
        <div class="span3">
          <img src="../assets/candidate1.jpg" width="100" height="100" alt="" class="img-polaroid" />
          <div class="roles">
            <h5><strong>Antonio Dutra</strong></h5>
            <input type="radio" name="candidate">
            <p>
              Partido de Direita
            </p>
          </div>
        </div>
        <div class="span3">
          <img src="../assets/candidate2.jpg" width="100" height="100" alt="" class="img-polaroid" />
          <div class="roles">
            <h5><strong>Joao da Silva</strong></h5>
            <input type="radio" name="candidate">
            <p>
              Partido de Esquerda
            </p>
          </div>
        </div>
        <div class="span3">
          <input type="submit" value="Selecione o seu candidato">
        </div>
      </div>
    </div>
  </section>
  <!-- end section about -->

  <a href="#" class="scrollup"><i class="icon-chevron-up icon-square icon-48 active"></i></a>

  </div>
</template>

<script>
export default {
  name: 'Candidate',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
