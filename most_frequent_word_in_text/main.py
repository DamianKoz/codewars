import re
import codewars_test as test


def top_3_words(text):
    text = re.sub(r"[^(\w|')]", " ", text)
    words = text.strip().lower().split(" ")
    print(f"TEXT: \n{text}\nWORDS: \n{words}")
    counts = dict()
    for word in words:
        word = word.strip()
        if word in counts:
            counts[word] = counts[word] + 1
        elif word and is_valid_word(word):
            counts[word] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_counts)
    print([elem[0] for elem in sorted_counts[:3]])
    return [elem[0] for elem in sorted_counts[:3]]


def is_valid_word(word):
    return re.match("^[a-zA-Z]*('[a-zA-Z]+)*$", word) is not None


@test.describe("Top 3 words")
def desc1():
    @test.it("Sample tests")
    def it1():
        test.assert_equals(
            top_3_words(
                "jiHIAU _VrloFIOlm !  ujjtenDLt    RLyC _ ??gIkqbChllc   VMwg    jiHIAU !  RLyC     bYeZifvD  _? bYeZifvD    VrloFIOlm?  gHQ gHQ_gHQ? VrloFIOlm ! abyLW!jiHIAU RLyC   VrloFIOlm vWxBpgiNi  ujjtenDLt  ! ujjtenDLt_   _gHQ  __gHQ jiHIAU ujjtenDLt_ !_MbJHborPXD ?   RLyC   abyLW   gIkqbChllc _VrloFIOlm!   !MbJHborPXD !  ?jiHIAU abyLW _   VrloFIOlm_ujjtenDLt VMwg!  _MbJHborPXD  abyLW _!bYeZifvD  ?RLyC ?_  ujjtenDLt   RLyC   ! jiHIAU_   bYeZifvD jiHIAU  abyLW ? VrloFIOlm_ujjtenDLt ?gHQ    abyLW   ?ujjtenDLt MbJHborPXD! !  VrloFIOlm!gIkqbChllc  VrloFIOlm_   RLyC     bYeZifvD   uYWegnRjK RLyC _DfkQKlxiNp   ! uYWegnRjK MbJHborPXD!bYeZifvD  RLyC!?_? VrloFIOlm_ _? bYeZifvD vWxBpgiNi  ujjtenDLt! bYeZifvD    gIkqbChllc! vWxBpgiNi_ujjtenDLt?_  uYWegnRjK_ ujjtenDLt MbJHborPXD   _ujjtenDLt _ ? uYWegnRjK  ? gIkqbChllc ?  _ujjtenDLt     vWxBpgiNi   abyLW    ?bYeZifvD!ujjtenDLt  __MbJHborPXD DfkQKlxiNp_   jiHIAU!    uYWegnRjK MbJHborPXD ?VMwg ?ujjtenDLt!?_ MbJHborPXD vWxBpgiNi ??  bYeZifvD! VrloFIOlm? gHQ   _DfkQKlxiNp _DfkQKlxiNp  abyLW _ abyLW?uYWegnRjK_ _ ?gHQ_VrloFIOlm_?   bYeZifvD  ? !bYeZifvD  MbJHborPXD    DfkQKlxiNp uYWegnRjK  RLyC   RLyC   ?RLyC_ vWxBpgiNi   DfkQKlxiNp gHQ  _RLyC_gIkqbChllc  _  gHQ  gHQ  _abyLW     ujjtenDLt   !RLyC!   uYWegnRjK? ? uYWegnRjK gIkqbChllc _? jiHIAU  RLyC_vWxBpgiNi   RLyC_    gHQ !! DfkQKlxiNp ujjtenDLt_ !_ abyLW_ujjtenDLt  DfkQKlxiNp    MbJHborPXD _??VrloFIOlm _RLyC  _uYWegnRjK ? _gHQ?  ujjtenDLt ? abyLW   _ VMwg    abyLW!    VrloFIOlm abyLW  _bYeZifvD? ! ?uYWegnRjK  ?VrloFIOlm?   abyLW VMwg  ? gHQ   MbJHborPXD_MbJHborPXD     gHQ_!   abyLW jiHIAU  ! !ujjtenDLt ujjtenDLt  jiHIAU  uYWegnRjK!   MbJHborPXD   bYeZifvD?  MbJHborPXD _VrloFIOlm_! ?gHQ   ! RLyC _  RLyC   ujjtenDLt _  _abyLW ?   gHQ  !_DfkQKlxiNp!?! VMwg   ?jiHIAU    bYeZifvD _?  MbJHborPXD   gHQ_  VMwg     "
            ),
            ["ujjtendlt", "rlyc", "ghq"],
        )
